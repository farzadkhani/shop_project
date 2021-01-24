from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from Products import models as products_models
from . import models as siteview_models


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = products_models.Category.objects.all()
        context['baner_slide'] = siteview_models.FirstSlideIndex.objects.filter(draft=False)
        return context
    

