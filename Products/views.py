from django.shortcuts import render
from django.views.generic import DetailView , ListView, FormView
from .models import Category, Product, ProductMeta, ShopProduct, Image, ProductMeta, Off, Brand
from Accounts.models import Shop
from siteview.forms import ProductForm
from django.shortcuts import get_object_or_404

# Create your views here.

class ProductList(ListView, FormView):
    model = Product
    queryset = Product.objects.all()    #base queryset
    form_class = ProductForm    #search form
    template_name = 'product_list.html'
    #paginate_by = 9        #for paginating
    #slug_url_kwarg = 'slug'
    #slug = self.kwargs.get(self.slug_url_kwargs)
        #def get_queryset(self):
        #category = get_object_or_404(Category, slug=slug)
        #self.kwargs['category'] = category
        #return category.get_products

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name', None)       #for search
        if name:
            query1 = Product.objects.filter(name__icontains=name)
            query2 = Product.objects.filter(brand__name__icontains=name)
            #query3 = Product.objects.filter(name__icontains=name)
            queryset = (query1 | query2).distinct()     #union two queryset
        
        if self.kwargs.get('slug', None):       #for get sub category prouduct
            category = Category.objects.filter(slug = self.kwargs['slug'])  #get curent page object with slug
            temprory_list = category[0].get_all_childrens()
            final_category_list = [category[0]]
            category_chil_list = []
            counter_for_temprory_list = len(temprory_list)

            while counter_for_temprory_list > 0:
                len_of_temprory_list = len(temprory_list)
                i_list = range(len_of_temprory_list)
                delet_list = []
                list_0 = []
                
                for i in i_list:                    
                    list_0 = [temprory_list[i], *list(list_0)]    #append curent page object to end of childrens object list
                    list_0 = [*list(list_0), *list(temprory_list[i].get_all_childrens())]    #get curent page list of childrens object with curent page object
                    delet_list = [*list(delet_list), temprory_list[i]]

                temprory_list = [*list(list_0)]
                temprory_list = list(set(temprory_list) - set(delet_list))
                category_chil_list = [*list(category_chil_list), *list(list_0)]
                list_0 = []
                counter_for_temprory_list = len(temprory_list)
            
            final_category_list = [*list(final_category_list) ,*list(category_chil_list)]
            queryset = queryset.filter(category__in = final_category_list).order_by('-publish_time')    #use category list  to filter get products with slug of curent page 
      
        brand_filter = self.request.GET.get('brand_filter')    #for filter
        if brand_filter:
            queryset = queryset.filter(brand__name=brand_filter)

        order_by = self.request.GET.get('order_by')     #for sort by date
        if order_by:
            queryset = queryset.order_by(order_by)
        #print(queryset[0].Off)
        
        #order_by_ = self.request.GET.get('order_by')     #for sort by price
        #print('order_by', order_by)
        #if order_by:
        #    queryset = queryset.order_by(order_by)
        
        #print(queryset)
        return queryset

    #def get_ordering(self):
    #    ordering = self.request.Get.get('publish_time', '-publish_time')
    #    return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(self.kwargs['slug'])  #print curent page slug 

        #<find the brand list>
        for_clean_list = context['object_list']
        clean_list = []
        for i in for_clean_list:
            if i.brand not in clean_list:
                clean_list.append(i.brand)
        context['clean_brand'] = clean_list
        #<end find brand list>

        #<find the all parent categoty>
        current_category = Category.objects.filter(slug=self.kwargs['slug'])
        current_category_parent_list = []
        current_category_parent_list.append(current_category[0])
        while current_category[0].get_all_parents() :
            current_category_parent_list.insert(0, current_category[0].get_all_parents()[0])
            current_category = current_category[0].get_all_parents()
        context['current_category'] = current_category_parent_list
        #<end find the all parent categoty>

        context['curent_slug_object'] = Category.objects.filter(slug=self.kwargs['slug'])
        context["category_list"] = Category.objects.all()
        context["product_meta_list"] = ProductMeta.objects.filter(product=context['object_list'])
        #context["shop_product_list"] = ShopProduct.objects.filter(product=context['object_list'])  #is_public=True
        #context["product_off_list"] = Off.objects.filter(product=context['object_list'])
        context["product_meta_list"] = ProductMeta.objects.filter(product=context['object_list'])

        #<calculate off percent>
        context['off_percent_list'] = {}
        for current_product in context['object_list']:
            if Off.objects.filter(product_id=current_product.id):
                product_prcie = ShopProduct.objects.filter(product_id=current_product.id)[0].price
                off_price = Off.objects.filter(product_id=current_product.id)[0].price
                off_percent = int((product_prcie - off_price)*100/product_prcie)
                context['off_percent_list'][current_product.id] = off_percent
        
        #<end calculate off percent>

        #context["product_images_list"] = Image.objects.filter(product=context['object_list'])
        #context['filter_form'] = forms.FilterListView(self.request.GET)
        #get_copy = self.request.GET.copy()
        #if get_copy.get('page'):
        #    get_copy.pop('page')
        #context['get_copy'] = get_copy
        #print(context['object_list'])
        return context
    
class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #<find the all parent categoty>
        current_product = Product.objects.filter(slug=self.kwargs['slug'])
        current_product_category_name = current_product[0].category
        current_category = Category.objects.filter(name=current_product_category_name)
        current_category_parent_list = []
        current_category_parent_list.append(current_category[0])
        while current_category[0].get_all_parents() :
            current_category_parent_list.insert(0, current_category[0].get_all_parents()[0])
            current_category = current_category[0].get_all_parents()
        context['current_category'] = current_category_parent_list
        #<end find the all parent category>
        context["category_list"] = Category.objects.all()
        #<product image from Image class>
        product_image = Image.objects.filter(product_id=current_product[0].id)
        context['product_image'] = product_image
        #<end product image from Image class>
        #<calculate off percent>
        if Off.objects.filter(product_id=current_product[0].id):
            product_price = ShopProduct.objects.filter(product_id=current_product[0].id)
            off_price = Off.objects.filter(product_id=current_product[0].id)
            off_percent = int((product_price[0].price - off_price[0].price)*100/product_price[0].price)
            context['off_percent'] = off_percent
        #<end calculate off percent>
        #print('---')
        #print(self.kwargs['slug'])
        #print('---')
        #print('context', context)
        return context
    

    

#this is a bad way we need the on product list not one product_list with category_detail
#class CategoryDetail(DetailView):
#    model = Category
#    template_name = 'category_detail.html'
#    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["category_list"] = Category.objects.all()
#        print(kwargs)#for us to see the kwargs<category slug> in terminal
#        context["product_list"] = Product.objects.filter(category=kwargs['object'])
#        context["shop_product_list"] = Product.objects.filter()
#        context["shop_list"] = Shop.objects.all()
#        return context


