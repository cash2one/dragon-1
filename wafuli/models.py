#coding:utf-8
from django.db import models
from DjangoUeditor.models import UEditorField
from account.models import MyUser
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields.related import OneToOneField
from .data import *
from django.template.defaultfilters import default
from django.utils import timezone
import datetime
class Company(models.Model):
    name = models.CharField(u"平台名称",max_length=100,unique=True)
    level = models.CharField(u"安全评级",max_length=100)
    site = models.CharField(u"网站地址",max_length=100)
    capital = models.CharField(u"注册资金",max_length=100)
    address = models.CharField(u"所在地区",max_length=100)
    launch_date = models.CharField(u"上线时间",max_length=100)
    trusteeship = models.CharField(u"托管情况",max_length=100)
    background = models.CharField(u"平台背景",max_length=100)
    information = models.CharField(u"公司信息",max_length=200)
    logo = models.FileField(u"网站logo（260*78）", upload_to='logo/%Y/%m/%d',default='')
    class Meta:
        verbose_name_plural = u"合作平台"
        verbose_name = u"合作平台"
    def __unicode__(self):
        return self.name
class Base(models.Model):
    title = models.CharField(max_length=200, verbose_name=u"标题") 
    news_priority = models.IntegerField(u"优先级",default=3)
    pub_date = models.DateTimeField(u"创建时间", auto_now_add=True)
    view_count = models.IntegerField(u"浏览量", default=0)
    change_user = models.CharField(u"上次修改用户", max_length=200, blank=True)
    url = models.CharField(u"本页面地址",max_length=200)
    def is_new(self):
        now = datetime.datetime.now()
        days = (now-self.pub_date).days
        return days == 0
    class Meta:
        abstract = True
    def __unicode__(self):
        return self.title
class News(Base):
    state = models.CharField(u"项目状态", max_length=1, choices=STATE)
    pic = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name=u"标志图片上传")
    isonMobile = models.BooleanField(u'是否为移动端活动', default= False)
    exp_url = models.CharField(u"活动地址", blank=True, max_length=200)
    exp_code = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name=u"上传二维码")
    advert = models.ForeignKey("Advertisement",blank=True, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    #增加title、keywords、description等seo字段
    seo_title = models.CharField(max_length=200, verbose_name=u"SEO标题", blank=True)
    seo_keywords = models.CharField(max_length=200, verbose_name=u"SEO关键词", blank=True)
    seo_description = models.CharField(max_length=200, verbose_name=u"SEO描述", blank=True)
    class Meta:
        abstract = True
    def clean(self):
        if self.isonMobile == False and self.exp_url == '':
            raise ValidationError({'exp_url': u'请输入活动体验地址'})
        elif self.isonMobile == True and self.exp_code == '':
            raise ValidationError({'exp_code': u'请上传手机扫描二维码'})
    def is_expired(self):
        return self.state == '2'
class ZeroPrice(News):
    provider = models.CharField(u"商家", max_length=10)
    time_limit = models.CharField(u"活动时间", max_length=24)
    zero_type = models.CharField(max_length=1, choices=ZERO_TYPE, verbose_name=u"福利类型")
    strategy=UEditorField(u"活动内容", width=900, height=600, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    class Meta:
        verbose_name = u"免费福利"
        verbose_name_plural = u"免费福利"
        ordering = ["-news_priority", "-pub_date"]
class Task(News):
    amount_to_invest = models.IntegerField(u"投资金额")
    scroreToAdd = models.IntegerField(u"奖励积分")
    moneyToAdd = models.FloatField(u"奖励现金")
    provider = models.CharField(u"商家", max_length=10)
    time_limit = models.CharField(u"活动时间", max_length=24)
    rules =UEditorField(u"奖励规则", width=900, height=300, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    strategy =UEditorField(u"体验步骤", width=900, height=300, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    user_event = GenericRelation("UserEvent",related_query_name='task')
    def get_type(self):
        return u"体验福利"
    class Meta:
        verbose_name = u"体验福利"
        verbose_name_plural = u"体验福利"
        ordering = ["-news_priority", "-pub_date"]
class Finance(News):
    filter = models.CharField(u"项目系列", max_length=2, choices=FILTER)
    scrores = models.CharField(u"补贴积分", max_length=100)
    benefit = models.CharField(u"补贴收益", max_length=100)
    amount_to_invest = models.IntegerField(u"起投额度")
    investTime = models.CharField(u"标期长度", max_length=100)
    interest = models.CharField(u"官网利息",max_length=8)
    rules =UEditorField(u"奖励规则", width=900, height=300, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    strategy =UEditorField(u"体验步骤", width=900, height=300, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    user_event = GenericRelation("UserEvent",related_query_name='finance')
    def get_type(self):
        return u"理财福利"
    class Meta:
        verbose_name = u"理财福利"
        verbose_name_plural = u"理财福利"
        ordering = ["-news_priority", "-pub_date"]
class Commodity(models.Model):
    pic = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name=u"商品图片上传(190*165)")
    name = models.CharField(u"商品名称", max_length=100)
    price = models.IntegerField(u"价格")
    category = models.CharField(u"商品分类", max_length=8, choices=CATEGORY)
    item = models.CharField(u"商品子类", max_length=8, choices=ITEM)
    url = models.CharField(u"本页面地址",max_length=200)
    advert = models.ForeignKey("Advertisement",blank=True, null=True, on_delete=models.SET_NULL)
    rules =UEditorField(u"奖品介绍", width=900, height=300, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    strategy =UEditorField(u"兑换流程", width=900, height=300, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u"商品"
        verbose_name_plural = u"积分商品"
class CouponProject(models.Model):
    title = models.CharField(u"项目名称",max_length=30)
    endtime = models.DateField(u"截止日期")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"优惠券项目"
        verbose_name_plural = u"优惠券项目"
class Coupon(models.Model):
    user = models.ForeignKey(MyUser, related_name="user_coupons")
    type = models.CharField(max_length=1, choices=COUPON_TYPE, verbose_name=u"优惠券类型")
    amount = models.PositiveIntegerField()
    project = models.ForeignKey(CouponProject, related_name="coupons")
    introduction = models.TextField(u"使用说明",max_length=200)
    time = models.DateField(u"发放日期", auto_now_add=True)
    url = models.CharField(u"网站地址", default="http://www.wafuli.com/", max_length=100)
    exchange_code = models.CharField(u"兑换码", blank=True, max_length=50)
    is_used = models.BooleanField(u"是否已使用", default = False)
    user_event = GenericRelation("UserEvent",related_query_name='coupon')
    def __unicode__(self):
        return self.project.title + ':' + self.user.username
    class Meta:
        verbose_name = u"优惠券"
        verbose_name_plural = u"优惠券"
        ordering = ['-time']
    def clean(self):
        if self.type == '2' and self.exchange_code == '':
            raise ValidationError({'exchange_code': u'使用券的兑换码是必输项'})
    def is_to_expired(self):
        endTime = self.project.endtime
        today = datetime.date.today()
        dif = (endTime-today).days
        return dif <= 7 and dif >= 0
    def is_expired(self):
        endTime = self.project.endtime
        today = datetime.date.today()
        return endTime < today
class Message(models.Model):
    user = models.ForeignKey(MyUser, related_name="user_msgs")
    title = models.CharField(u"标题", max_length=30)
    time = models.DateTimeField(u"日期", default=timezone.now)
    is_read = models.BooleanField(u"是否已读", default=False)
    content = models.TextField(u"消息内容")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"消息"
        verbose_name_plural = u"消息"
        ordering = ['-time']
class UserEvent(models.Model):
    user = models.ForeignKey(MyUser, related_name="user_event_history")
#    event_level = models.PositiveIntegerField(u'事件级别（决定是否需审核）')
    event_type = models.CharField(max_length=10, choices=USER_EVENT_TYPE, verbose_name=u"用户事件类型")
    invest_account = models.CharField(u"第三方注册账号/提现账号", max_length=100)
    invest_amount = models.DecimalField(u'涉及金额', blank=True, null=True,decimal_places = 2, max_digits=10)
    time = models.DateTimeField(u'提交时间', default=timezone.now)
    audit_time = models.DateTimeField(u'审核时间', null=True, blank=True)
    audit_state = models.CharField(max_length=10, choices=AUDIT_STATE, verbose_name=u"审核状态")
    remark = models.CharField(u"备注", max_length=100,blank=True)
    content_type = models.ForeignKey(ContentType,null=True,blank=True)
    object_id = models.PositiveIntegerField(null=True,blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    def get_content_object(self):
        return self.content_object
    def __unicode__(self):
        return u"%s的用户事件：%s" % (self.user, self.get_event_type_display())
    class Meta:
        ordering = ["-time",]
# class Log_ZeoroPrice(BaseLog):
#     zeroprice = models.ForeignKey(ZeroPrice, related_name='history_related')
# class Log_Task(BaseLog):
#     task = models.ForeignKey(Task, related_name='history_related')
class AdminEvent(models.Model):
    admin_user = models.ForeignKey(MyUser, related_name="user_admin_history")
    custom_user = models.ForeignKey(MyUser, related_name="user_awarding_history")
    event_type = models.CharField(max_length=10, choices=ADMIN_EVENT_TYPE, verbose_name=u"管理员事件类型")
    time = models.DateTimeField(u'操作时间', auto_now_add=True)
    remark = models.CharField(u"备注", max_length=100)
    def __unicode__(self):
        return u"%s给%s做了%s操作,时间：%s" % (self.admin_user, self.custom_user, self.get_event_type_display(),
                                       self.time)
    class Meta:
        ordering = ["-time",]
        
class AuditLog(models.Model):
    user = models.ForeignKey(MyUser, related_name="audited_logs")
    item = models.ForeignKey(UserEvent, related_name="audited_logs")
    admin_item = models.ForeignKey(AdminEvent, related_name="audited_logs")
    time = models.DateTimeField(u'审核时间', auto_now_add=True)
    audit_result = models.BooleanField(default=False, verbose_name=u"审核结果")
    reason = models.CharField(u"备注（拒绝原因）", max_length=100,blank=True)
    def __unicode__(self):
        return u"审核员：%s,用户事件：%s，管理员事件:%s,审核结果：%s，审核时间：%s，提交时间：%s" % (self.user,self.item,
                        self.admin_item,self.audit_result, self.time, self.item.time)
    class Meta:
        ordering = ["-time",]
class TransList(models.Model):
    user = models.ForeignKey(MyUser, related_name="translist")
    time = models.DateTimeField(u'时间', auto_now_add=True)
    initAmount = models.DecimalField(u'变动前数值',decimal_places = 2, max_digits=10)
    transAmount = models.DecimalField(u'变动数值', decimal_places = 2, max_digits=10)
    reason = models.CharField(max_length=20, verbose_name=u"变动原因")
    remark = models.CharField(u"备注", max_length=100, blank=True)
    transType = models.CharField(max_length=2, choices=TRANS_TYPE, verbose_name=u"变动类型")
    user_event = models.ForeignKey(UserEvent, related_name="translist", null=True)
    admin_event = models.ForeignKey(AdminEvent, related_name="translist", null=True)
    def __unicode__(self):
        return u"%s:%s了%s现金 提交时间%s" % (self.user, self.get_transType_display(),self.transAmount,
                                       self.user_event.time if self.user_event else "")
    class Meta:
        ordering = ["-time",]

class ScoreTranlist(models.Model):
    user = models.ForeignKey(MyUser, related_name="score_translist")
    time = models.DateTimeField(u'时间', auto_now_add=True)
    initAmount = models.IntegerField(u'变动前数值')
    transAmount = models.IntegerField(u'变动数值')
    reason = models.CharField(max_length=20, verbose_name=u"变动原因")
    remark = models.CharField(u"备注", max_length=100,blank=True)
    transType = models.CharField(max_length=1, choices=TRANS_TYPE, verbose_name=u"变动类型")
    user_event = models.ForeignKey(UserEvent, related_name="score_translist", null=True)
    admin_event = models.ForeignKey(AdminEvent, related_name="score_translist", null=True)
    def __unicode__(self):
        return u"%s:%s了%s积分 提交时间%s" % (self.user, self.get_transType_display(),self.transAmount,
                                       self.user_event.time if self.user_event else "")
    class Meta:
        ordering = ['-time']

class ExchangeRecord(models.Model):
    tranlist = OneToOneField(ScoreTranlist, primary_key=True)
    commodity = models.ForeignKey(Commodity, related_name="exchange_record")
    name = models.CharField(u'收件人姓名', max_length=20)
    tel = models.CharField(u'收件人手机号', max_length=14)
    addr = models.CharField(u'收件人地址', max_length=100)
    message = models.CharField(u'留言', default=u"暂无", max_length=100)
    user_event = GenericRelation("UserEvent",related_query_name='exchangerecord')
    def __unicode__(self):
        return u"%s:收件人为 %s" % (self.tranlist.user, self.name)
    class Meta:
        ordering = ["-tranlist__time",]
    
class Press(Base):
    summary = models.TextField(verbose_name=u"摘要")
    type = models.CharField(u"新闻类型", max_length=1, choices=NEWS_TYPE)
    pic = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True,
                             verbose_name=u"新闻图片上传(110*72)")
    content=UEditorField(u"内容", width=900, height=300, toolbars="full", 
                         imagePath="photos/%(year)s/%(month)s/%(day)s/",
                         filePath="photos/%(year)s/%(month)s/%(day)s/", 
                         upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    #增加title、keywords、description等seo字段
    seo_title = models.CharField(max_length=200, verbose_name=u"SEO标题", blank=True)
    seo_keywords = models.CharField(max_length=200, verbose_name=u"SEO关键词", blank=True)
    seo_description = models.CharField(max_length=200, verbose_name=u"SEO描述", blank=True)
    def clean(self):
        if self.type == '3' and not self.pic:
            raise ValidationError({'pic': u'新闻类型必输'})
    class Meta:
        ordering = ["-news_priority","-pub_date"]
        verbose_name = u"新闻（公告、攻略等）"
        verbose_name_plural = u"新闻（公告、攻略等）"
class Advertisement(Base):
    pic = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False,
                             verbose_name=u"banner图片上传(1920*300)")
    location = models.CharField(u"广告位置", max_length=2, choices=ADLOCATION)
    is_hidden = models.BooleanField(u"是否隐藏",default=False)
    class Meta:
        ordering = ["-news_priority","-pub_date"]
        verbose_name = u"横幅广告"
        verbose_name_plural = u"横幅广告"
class UserWelfare(models.Model):
    user = models.ForeignKey(MyUser, related_name="submited_welfare")
    title = models.CharField(max_length=200, verbose_name=u"标题")
    url = models.CharField(u"福利地址",max_length=200)
    reason = models.CharField(u"推荐理由",max_length=200)
    date = models.DateTimeField(u"创建时间", auto_now_add=True)
    user_event = GenericRelation("UserEvent",related_query_name='submit_welfare_record')
    class Meta:
        ordering = ["-date"]
        unique_together = (('title', 'url'),)
    def __unicode__(self):
        return self.title + '+' + self.url
class Activity(Base):
    pic = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False,
                             verbose_name=u"banner图片上传(110*72)")
    summary = models.TextField(verbose_name=u"摘要")
    is_hidden = models.BooleanField(u"是否隐藏",default=False)
    class Meta:
        ordering = ["-news_priority","-pub_date"]
        verbose_name = u"热门活动"
        verbose_name_plural = u"热门活动"
        
class LotteryRecord(models.Model):
    user = models.ForeignKey(MyUser, related_name="lottery_record")
    award = models.CharField(u"奖品", max_length=20)
    date = models.DateTimeField(u"创建时间", auto_now_add=True, db_index=True)
    class Meta:
        ordering = ["-date"]
    def __unicode__(self):
        return u"%s中了%s" % (self.user, self.award)