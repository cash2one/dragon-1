'''
Created on 20160222

@author: lch
'''
from django.conf.urls import url,include

# url_about = [
#     url(r'^aboutus/$', 'wafuli.views.aboutus', name="about"),
#     url(r'^report/$', 'wafuli.views.report'),
#     url(r'^coop/$', 'wafuli.views.coop'),
#     url(r'^notice/$', 'wafuli.views.notice'),
#     url(r'^contact/$', 'wafuli.views.contact'),
#     url(r'^statement/$', 'wafuli.views.statement'),
# ]
urlpatterns = [
    url(r'^$', 'wafuli.views.index', name='index'),
#    url(r'^(?P<board>\S+)/$', 'wafuli.views.board', name='board'),
    url(r'^finance/$', 'wafuli.views.finance', name='finance'),
    url(r'^finance/(?P<id>[0-9]*)/$', 'wafuli.views.finance', name='finance_detail'),
    url(r'^task/$', 'wafuli.views.task', name='task'),
    url(r'^task/(?P<id>[0-9]*)/$', 'wafuli.views.task', name='task_detail'),
    url(r'^welfare/$', 'wafuli.views.welfare', name='welfare'),
    url(r'^welfare/(?P<id>[0-9]*)/$', 'wafuli.views.welfare', name='welfare_detail'),
    url(r'^mall/$', 'wafuli.views.mall', name='mall'),
    url(r'^commodity/(?P<id>[0-9]*)/$', 'wafuli.views.commodity', name='commodity_detail'),
    url(r'^press/(?P<id>[0-9]*)/$', 'wafuli.views.press', name='press_detail'),
    url(r'^mallpage/$', 'wafuli.views.get_commodity_page', name='get_commodity_page'),
    url(r'^financepage/$', 'wafuli.views.get_finance_page', name='get_finance_page'),
    url(r'^taskpage/$', 'wafuli.views.get_task_page', name='get_task_page'),
    url(r'^welpage/$', 'wafuli.views.get_wel_page', name='get_wel_page'),
    url(r'^presspage/$', 'wafuli.views.get_press_page', name='get_press_page'),
    url(r'^aboutus/', 'wafuli.views.aboutus', name="aboutus"),
    url(r'^exp/', 'wafuli.views.experience', name='exp'),
    url(r'^expsubmit/', 'wafuli.views.expsubmit', name='expsubmit'),
    url(r'^lookup_order/$', 'wafuli.views.lookup_order', name='lookup_order'),
    url(r'^submit_order/$', 'wafuli.views.submit_order', name='submit_order'),
    
    url(r'^freshman/introduction/$', 'wafuli.views.freshman_introduction', name='freshman_introduction'),
    url(r'^freshman/award/$', 'wafuli.views.freshman_award', name='freshman_award'),
    
    url(r'^activity/recommend/$', 'wafuli.activity.recommend', name='activity_recommend'),
    url(r'^activity/recompage/$', 'wafuli.activity.get_activity_recommend_page', name='get_activity_recommend_page'),
    url(r'^activity/recomrankpage/$', 'wafuli.activity.get_recommend_rank_page', name='get_recommend_rank_page'),
    
    url(r'^activity/lottery/$', 'wafuli.activity.lottery', name='activity_lottery'),
    url(r'^activity/lottery/get_lottery/$', 'wafuli.activity.get_lottery', name='get_lottery'),
]
