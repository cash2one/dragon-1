'''
Created on 20160417

@author: zhlvch
'''

import logging
import time,datetime
from django.db import connection
from django.db.models import Sum, Count,Avg
from dircache import annotate
from wafuli.models import ZeroPrice, Task, Finance
logger = logging.getLogger("wafuli")
from django.core.management.base import BaseCommand, CommandError
from account.models import MyUser, Userlogin
from wafuli.models import UserEvent
from wafuli_admin.models import DayStatis, RecommendRank, GlobalStatis
class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("******Statistics on every day night is beginning*********")
        begin_time = time.time()
        today = datetime.date.today() 
        yesterday = today - datetime.timedelta(days=1)
        dict = MyUser.objects.filter(date_joined__gte=today).aggregate(count=Count('id'))
        new_reg_num = dict.get('count')
        dict = Userlogin.objects.filter(time__gte=today).aggregate(num=Count('user',distinct=True))
        active_num = dict.get('num')
        dict = UserEvent.objects.filter(audit_time__gte=today,event_type='2',audit_state='0').\
                aggregate(cou=Count('user_id',distinct=True),sum=Sum('invest_amount'))
        with_amount = dict.get('sum') or 0
        with_num = dict.get('cou')
        dict = UserEvent.objects.filter(audit_time__gte=today,event_type='1',audit_state='0').\
                aggregate(cou=Count('user_id',distinct=True),sum1=Sum('translist__transAmount'),sum2=Sum('score_translist__transAmount'))
        ret_amount = dict.get('sum1') or 0
        ret_num = dict.get('cou')
        ret_scores = dict.get('sum2') or 0
        dict = UserEvent.objects.filter(audit_time__gte=today,event_type='3',audit_state='0').\
                aggregate(cou=Count('user_id',distinct=True),sum=Sum('invest_amount'))
        exchange_scores = dict.get('sum') or 0
        exchange_num = dict.get('cou')
        new_wel_num = ZeroPrice.objects.filter(pub_date__gte=today).count() + \
                Task.objects.filter(pub_date__gte=today).count() + \
                Finance.objects.filter(pub_date__gte=today).count()
        update_fields = {
                         'new_reg_num':new_reg_num,
                         'active_num':active_num,
                         'with_amount':with_amount,
                         'with_num':with_num,
                         'ret_amount':ret_amount,
                         'ret_scores':ret_scores,
                         'ret_num':ret_num,
                         'exchange_num':exchange_num,
                         'exchange_scores':exchange_scores,
                         'new_wel_num':new_wel_num,
        }
        DayStatis.objects.update_or_create(date=today, defaults=update_fields)
        
        first_day = datetime.datetime(today.year, today.month, 1)
        item_list = UserEvent.objects.filter(time__gte=first_day,event_type='6',audit_state='0').values('user').\
            annotate(cou=Count('*'),award=Sum('translist__transAmount')).order_by('user')
        for dic in item_list:
            user_id = dic.get('user')
            count = dic.get('cou')
            award = dic.get('award') or 0
            user=MyUser.objects.get(id=user_id)
            RecommendRank.objects.update_or_create(user=user,defaults={'award':award,'acc_num':count})
        ranks = RecommendRank.objects.all().order_by("-acc_num")
        i = 1
        n = 0
        j = 0
        for r in ranks:
            if r.acc_num == n:
                r.rank = i
            else:
                i = i + j
                r.rank = i
                j = 0
            j = j + 1
            n = r.acc_num
            r.save(update_fields=['rank'])
        
#         dict_with = UserEvent.objects.filter(event_type='2',audit_state='0').\
#             aggregate(cou=Count('user',distinct=True),sum=Sum('translist__transAmount'))
        total_award = MyUser.objects.aggregate(sum=Sum('accu_income'))
        global_statis = GlobalStatis.objects.first()
        if not global_statis:
            global_statis = GlobalStatis()
        global_statis.all_wel_num = ZeroPrice.objects.count() + Task.objects.count() + Finance.objects.count()
        global_statis.award_total = total_award.get('sum')
        global_statis.save()
        
        end_time = time.time()
        logger.info("******Statistics is finished, time:%s*********",end_time-begin_time)