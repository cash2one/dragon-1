from django.contrib import admin
from .models import MyUser
from .forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth.admin import UserAdmin
from account.models import UserSignIn, Userlogin, Access_Token, MobileCode,\
    AdminPermission
# Register your models here.
class MyUserAdmin(UserAdmin):
# The forms to add and change user instances
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    # The fields to be used in displaying the User model.
    fieldsets = (
        (None, {'fields': ('email', 'mobile','username','password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions', 'admin_permissions')}),
        ('Important dates', {'fields': ('last_login_time', 'date_joined', 'invite_code')}),
        ('others', {'fields': ('accu_income','accu_scores','balance','scores','invite_account','invite_income',
                               'invite_scores','inviter','isSigned', 'last_login_time', 'this_login_time',
                               'pay_password','is_email_authenticated','zhifubao','zhifubao_name')}),
    )
    add_fieldsets = (
    (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'username','password1', 'password2')}
            ),
    )
    search_fields = ('mobile','email','username')
    ordering = ('mobile',)
    list_display = ('mobile', 'email', 'username','is_staff','date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(UserSignIn)
admin.site.register(Userlogin)
admin.site.register(Access_Token)
admin.site.register(MobileCode)
admin.site.register(AdminPermission)
