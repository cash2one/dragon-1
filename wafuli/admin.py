#coding:utf-8
from django.contrib import admin

# Register your models here.
from .models import *
from .tools import writeHtml,createUrl
from django.http.response import Http404

from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
#     fields = ('title', 'pic1', 'pic2', 'pic3', 'content', 'url')
    search_fields = ['title',]
    list_filter = ['news_priority', 'change_user',]
    def save_model(self, request, obj, form, change):
        obj.change_user = str(request.user)
        if obj.advert is None:
            obj.advert = Advertisement.objects.filter(location='7',is_hidden=False).first()
        obj.save()
class FinanceAdmin(NewsAdmin):
    readonly_fields = ('url','pub_date','change_user')
    def save_model(self, request, obj, form, change):
        super(FinanceAdmin,self).save_model (request, obj, form, change)
        if not change:
            obj.url = reverse('finance_detail', kwargs={'id': obj.pk})
            obj.save(update_fields=['url',])
class TaskAdmin(NewsAdmin):
    readonly_fields = ('url','pub_date','change_user')
    def save_model(self, request, obj, form, change):
        super(TaskAdmin,self).save_model (request, obj, form, change)      
        if not change:
            obj.url = reverse('task_detail', kwargs={'id': obj.pk})
            obj.save(update_fields=['url',])
class CommodityAdmin(NewsAdmin):
    search_fields = ['name',]
    list_filter = []
    readonly_fields = ('url',)
    def save_model(self, request, obj, form, change):
        super(CommodityAdmin,self).save_model (request, obj, form, change)   
        if not change:
            obj.url = reverse('commodity_detail', kwargs={'id': obj.pk})
            obj.save(update_fields=['url',])
class ZeroAdmin(NewsAdmin):
    readonly_fields = ('url','pub_date','change_user')
    def save_model(self, request, obj, form, change):
        super(ZeroAdmin,self).save_model (request, obj, form, change) 
        if not change:
            obj.url = reverse('welfare_detail', kwargs={'id': obj.pk})
            obj.save(update_fields=['url',])
class PressAdmin(NewsAdmin):
    readonly_fields = ('pub_date','change_user','url')
    def save_model(self, request, obj, form, change):
        obj.change_user = str(request.user)
        obj.save()
        if not change:
            obj.url = reverse('press_detail', kwargs={'id': obj.pk})
            obj.save(update_fields=['url',])
class ComAdmin(admin.ModelAdmin):
    search_fields = ['name', 'level','site','capital','address','launch_date','trusteeship','background',]
class UserEventAdmin(admin.ModelAdmin):
    search_fields = ()
    list_display = ('user','content_object', 'invest_account','time','event_type','audit_state')
class ActivityAdmin(admin.ModelAdmin):
#     fields = ('title', 'pic1', 'pic2', 'pic3', 'content', 'url')
    search_fields = ['title',]
    list_filter = ['news_priority', 'change_user',]
    def get_readonly_fields(self, request,obj=None):  
        fields=[]  
        if request.user.is_superuser:  
            return fields  
        else:  
            fields=['change_user']
            return fields  

admin.site.register(Finance,FinanceAdmin)
admin.site.register(Company, ComAdmin)
admin.site.register(ZeroPrice, ZeroAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Commodity,CommodityAdmin)
admin.site.register(UserEvent, UserEventAdmin)
admin.site.register(AuditLog)
admin.site.register(AdminEvent)
admin.site.register(ScoreTranlist)
admin.site.register(TransList)
admin.site.register(ExchangeRecord)
admin.site.register(Press,PressAdmin)
admin.site.register(CouponProject)
admin.site.register(Coupon)
admin.site.register(Message)
admin.site.register(Advertisement)
admin.site.register(UserWelfare)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(LotteryRecord)