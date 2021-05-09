from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from Products.models import Category, Product, Brand
from .models import FirstSlideIndex

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baner_slide'] = FirstSlideIndex.objects.filter(draft=False)
        context['baner_slide_counter'] = FirstSlideIndex.objects.filter(draft=False).count()-1
        context['amazing_offer'] = Product.objects.filter(is_amazing_offer=True)
        # context["category_list"] = Category.objects.all()
        context["special_brand_list"] = Brand.objects.filter(is_special=True)
        context["top_category"] = Category.objects.filter(parent__isnull=True)


        return context
