from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings


# Create your models here.
class FirstSlideIndex(models.Model):
    image = models.ImageField(_("image"), upload_to='siteview/firstslideindex/images')
    title_one = models.CharField(_('product title one'), max_length=500)
    title_two = models.CharField(_('product title two'), max_length=500)
    detail = models.CharField(_('product detail'), max_length=500)
    draft = models.BooleanField(_('Draft'), default=True, db_index=True)
    
    class Meta:
        verbose_name = _('FirstSlideIndex')
        verbose_name_plural = _('FirstSlideIndex')
        
    def __str__(self):
        return self.detail