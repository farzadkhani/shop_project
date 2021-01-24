from django.contrib import admin
from django.contrib.admin.sites import site
from django.utils.translation import ugettext_lazy as _
from . import models
# Register your models here.


@admin.register(models.FirstSlideIndex)
class FirstSlideIndexAdmin(admin.ModelAdmin):
    list_display = ('title_one','title_two', 'draft')    
    search_fields = ('title_one','title_two', 'draft')
    list_filter = ('draft',)