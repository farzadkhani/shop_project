from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from Products.models import Category
from .models import FirstSlideIndex

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baner_slide'] = FirstSlideIndex.objects.filter(draft=False)
        context["category_list"] = Category.objects.all()
        return context
