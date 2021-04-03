from django.shortcuts import render, get_object_or_404, redirect
from .models import BasketItems, Basket
from Products.models import Product, ShopProduct, Category
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.contrib import messages
# Create your views here.

#class BasketDetail(DetailView):
#    model = Basket
#    template_name = 'basket.html'

class BasketItemList(ListView):
    model = Basket
    template_name = 'basket.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        context["category_list"] = Category.objects.all()
        # context['curent_slug_object'] = Category.objects.filter(slug=self.kwargs['slug'])
        # print('kwargs', self.kwargs)
        # print('context', context['object_list'][0].basket_items[0])
        print('object list', context['object_list'])
        return context
    

def add_to_basket(request, slug, id):
    shopproduct = get_object_or_404(ShopProduct, id=id)
    basket_qs = Basket.objects.filter(user=request.user)
    #check basket is exist
    if basket_qs.exists():
        basket = basket_qs[0]
        # check basket_item is in the basket
        if BasketItems.objects.filter(shopproduct=shopproduct, basket=basket).exists():
            basket_item = BasketItems.objects.get(shopproduct = shopproduct, basket=basket)
            basket_item.quantity += 1
            basket_item.save()
            messages.info(request, 'تعداد محصول افزایش پیدا کرد')
        else:
            basket_item = BasketItems.objects.create(shopproduct=shopproduct, basket=basket)
            messages.info(request, 'این محصول به سبد شما اضافه شد')

    else:
        basket = Basket.objects.create(user=request.user)
        basket_item = BasketItems.objects.create(shopproduct=shopproduct, basket= basket)
        messages.info(request, 'این محصول به سبد شما اضافه شد')
        #basket_item.add(basket_item)
    return redirect('detail_product', slug=slug, id=id)
  

def remove_from_basket(request, id):
    basket_item = BasketItems.objects.get(shopproduct__id = id, basket__user=request.user)
    basket_item.delete()
    #print(basket_item[0].quantity)
    messages.info(request, 'این محصول از سبد شما حذف شد')
    return redirect('basket')


def decrease_from_basket(request, id):
    basket_item = BasketItems.objects.get(shopproduct__id = id, basket__user=request.user)
    if basket_item.quantity > 1:
        basket_item.quantity -= 1
        basket_item.save()
        messages.info(request, 'تعداد محصول کاهش پیدا کرد')
        return redirect('basket')
    else:
        basket_item.delete()
        messages.info(request, 'این محصول از سبد شما حذف شد')
        return redirect('basket')


def increase_from_basket(request, id):
    basket_item = BasketItems.objects.get(shopproduct__id = id, basket__user=request.user)
    basket_item.quantity += 1
    basket_item.save()
    messages.info(request, 'تعداد محصول افزایش پیدا کرد')
    return redirect('basket')

