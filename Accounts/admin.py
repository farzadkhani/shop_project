from django.contrib import admin
from .models import User, Address, Shop, Email #Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)  #way like this?
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.forms import AdminPasswordChangeForm
# Register your models here.

@admin.register(User)
class UserAdmin (BaseUserAdmin):
    fieldsets = (   #settings for admin page in person
        ('authentication:', {'fields': ('email', 'mobile', 'first_name', 'last_name', 'password')}),
        (_('Your personal info:'), {'fields': ('image',)}),
        (_('Your permissions:'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Your important dates:'), {'fields': ('date_joined', 'last_login')}), # 
    )
    
    add_fieldsets = (   #settings for admin page add the new person
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile' 'first_name', 'last_name', 'image', 'is_superuser',
            'is_staff', 'groups', 'user_permissions','password1', 'password2'),
        }),
    )

    
    list_display = ('email', 'mobile', 'is_staff', 'is_active', 'last_login')
    #settings for admin page in group
    #show the 'username'and 'imail' in admin list
    ordering =('email',)
#    search_fields = ('email',)
#    filter_horizontal = ()
#    change_password_form = AdminPasswordChangeForm
admin.site.register(User, UserAdmin)

@admin.register(Address)
#class AddressAdmin(admin.ModelAdmin):
#    list_display = ('user','city','street','allay','zip_code')
#    list_filter = ('city')
#    list_editable
#    list_display_links
#    list_max_show_all
#    list_per_page
#    list_select_related

#def make_published(modeladmin, request, queryset):
#    queryset.update(daft=False)

#make_published.short_description = "Mark selected stories as published"

#admin.site.register(AdressAdmin, UserAdmin)
#
#@admin.register(Useremail)
#class UserEmailAdmin(admin.ModelAdmin):
#    list_display = ('to_user','subject','body')
#admin.site.register(UserEmailAdmin, UserAdmin)
#
#@admin.register(Shop)
#class ShopAdmin(admin.ModelAdmin):
#    list_display = ('user','name','slug','discreption','image')
#    actions = [make_published]
#    action_form
#    actions_on_bottom
#    actions_on_top
#    actions_selection_counter
#admin.site.register(ShopAdmin, UserAdmin)
