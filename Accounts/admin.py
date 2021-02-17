from django.contrib import admin
from .models import User, Address, Shop, Email ,Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)  
#way like this?
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
    
    add_fieldsets = (   
    #settings for admin page add the new person
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'first_name', 'last_name', 'image', 'is_superuser',
            'is_staff', 'groups', 'user_permissions','password1', 'password2'),
        }),
    )
    
    list_display = ('email', 'mobile', 'is_staff', 'is_active', 'last_login')
    #settings for admin page in group
    #show the 'username'and 'imail' in admin list
    ordering =('email',)
    search_fields = ('email',)
#    filter_horizontal = ()
    change_password_form = AdminPasswordChangeForm
#admin.site.register(User, UserAdmin)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user','city','street','zip_code')
    list_filter = ('city',)
    search_fields = ('zip_code',)
    #list_editable
    #list_display_links
    #list_max_show_all
    #list_per_page
    #list_select_related
#    def make_publishe(ModelAdmin, request, queryset):
#        queryset.update(daft=False)
#        make_published.short_description = "Mark selected stories as published"
#admin.site.register(Address, AddressAdmin)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('user','slug','name', 'is_active')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user',)

    #def get_fields(self, request, obj=None):
    #    fields = super().get_fields(request, obj)
    #    if request.user.is_superuser or request.user:
    #        fields += ('user',)
    #    return fields
    #list_editable
    #list_display_links
    #list_max_show_all
    #list_per_page
    #list_select_related
#    def make_publishe(ModelAdmin, request, queryset):
#        queryset.update(daft=False)
#        make_published.short_description = "Mark selected stories as published"
#admin.site.register(Shop, ShopAdmin)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('user','to','subject')
#admin.site.register(UserEmail, UserEmailAdmin)

