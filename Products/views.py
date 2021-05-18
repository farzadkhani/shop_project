# from pprint import pprint
from django.contrib.auth.mixins import LoginRequiredMixin
from Accounts.models import Shop
from django.db.models import Q
# Avg, Max, Min,
# from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
# render,
from django.views.generic import DetailView, ListView, CreateView, UpdateView, View
# FormView,
from django.views.generic.edit import FormMixin
from siteview.forms import ProductForm
# ProductAttrsForm,
from .models import (
    Category, Image, Product, ShopProduct, Size,
    Color, WishList, Comment, CommentLike, CommentDisLike
    )
# Brand, Off, ProductMeta,
from .forms import SellerShopProductForm, CommentForm
# from .filters import ProductListFilter
from django.urls import reverse_lazy
from django.contrib import messages
# from Accounts.models import User

# Create your views here.



# filters = {}

# for key, value in request.post.items():
#     if key in ['filter1', 'filter2', 'filter3']:
#         filters[key] = value

# Test.objects.filter(**filters)

# if request.method == 'GET':
#         filters = {}
#         for key, value in request.GET.items():
#             if value != '':
#                 filters[key] = value
#         filter_list=Pet.objects.filter(**filters)

class SearchInProducts(FormMixin, ListView):
    model = Product
    form_class = ProductForm
    template_name = 'product_list_category.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        url_addres = self.request.path_info.format
        print('url is:', url_addres)
        name = self.request.GET.get('q', None)  # for search
        if name:
            queryset = queryset.filter(Q(name__icontains=name)|Q(brand__name__icontains=name))

        brand_filter = self.request.GET.get('brand_filter')  # for filter
        # print('brand', brand_filter)
        if brand_filter:
            queryset = queryset.filter(brand__name=brand_filter)

        order_by = self.request.GET.get('order_by')  # for sort by date
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        context["category_list"] = Category.objects.all()

        # <find the brand list>
        for_clean_list = context['object_list']
        clean_list = []
        for i in for_clean_list:
            if i.brand not in clean_list:
                clean_list.append(i.brand)
        context['clean_brand'] = clean_list
        # <end find brand list>

        # <the search name>
        context['search_name'] = self.request.GET.get('q')
        # <end the search name>

        # <the price range>
        name = self.request.GET.get('q')  # for search
        qs = Product.objects.filter(Q(name__icontains=name)|Q(brand__name__icontains=name))
        # print('qs: ', len(qs))
        qs_list = []
        for i in qs:
            if i.find_all_size_and_color:
                # print('i: ', i.id)
                qs_list.append(i)
                # print('qs list: ', qs_list)
        qsd = sorted(qs_list, key=lambda t: t.first_min_price)
        # print('price', qsd[0].first_min_price)
        if len(qsd) > 0:
            context['first_price_range'] = qsd[0]
            context['last_price_range'] = qsd[-1]
        # < end the price range>
        return context


class ProductListCategory(ListView):    # , FormView, FormMixin, 
    model = Product
    paginate_by = 9
    queryset = Product.objects.all()  # base queryset
    template_name = 'product_list_category.html'
    # paginate_by = 9        # for paginating

    # def is_valid_queryparam(param):
    #     return param != "" and param is not None

    def get_queryset(self):
        # print(self.request.get_full_path())
        queryset = super().get_queryset()

        if self.kwargs.get('slug', None):  # for get sub category prouduct
            category_object = Category.objects.get(slug=self.kwargs['slug'])
            final_category_list = category_object.get_all_sub_childrens_
            final_category_list = [*list(final_category_list), category_object]
            queryset = queryset.filter(category__in=final_category_list).order_by(
                '-publish_time')  
            # use category list  to filter get products with slug of curent page
        
        brand_filter = self.request.GET.get('brand_filter')
        order_by = self.request.GET.get('order_by')

        if brand_filter!='' and brand_filter is not None:
            queryset = queryset.filter(brand__name=brand_filter)

        if order_by!='' and order_by is not None:
            if order_by == '-publish_time' or order_by== 'publish_time':
                queryset = queryset.order_by(order_by)
            elif order_by == 'price':
            # queryset = queryset.order_by('-ShopProduct__price').values_list('id', flat=True).distinct()
                items, item_ids = [], []
                for item in queryset.order_by('-ShopProduct__price'):
                    print('item is: ', item.id)
                    if not item in item_ids:
                        items.append(item)
                        item_ids.append(item)
                        queryset = item_ids
                print('list item_ids', item_ids)
            else:
            # queryset = queryset.order_by('ShopProduct__price').values_list('id', flat=True).distinct()
                items, item_ids = [], []
                for item in queryset.order_by('ShopProduct__price'):
                    print('item is: ', item.id)
                    if not item in item_ids:
                        items.append(item)
                        item_ids.append(item)
                        queryset = item_ids
                print('list item_ids', item_ids)


        # product_filter_list = ProductListFilter(self.request.GET, queryset=queryset)
        # return product_filter_list.qs

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.kwargs['slug'])  #print curent page slug 
        # print(self.kwargs)  #print all in kwargs
        # print('the request contain: ', self.request)  #print all in kwargs
        # print('the request.path contain: ', self.request.path)  #print all in kwargs

        # <filter form>
        # context['filter'] = ProductListFilter(self.request.GET, queryset=self.get_queryset())
        # print("filter context: ", context['filter'].form["name"])
        # <end filter form>
        
        # print(self.kwargs)

        # <find the brand list>
        for_clean_list = context['object_list']
        clean_list = []
        for i in for_clean_list:
            if i.brand not in clean_list:
                clean_list.append(i.brand)
        context['clean_brand'] = clean_list
        # <end find brand list>

        context['curent_slug_object'] = Category.objects.filter(slug=self.kwargs['slug'])
        context["category_list"] = Category.objects.all()
        # context["shop_product_list"] = ShopProduct.objects.filter(product=context['object_list'])  #is_public=True
        # context["product_off_list"] = Off.objects.filter(product=context['object_list'])
        # context["product_meta_list"] = ProductMeta.objects.filter(product=context['object_list'])

        # <the price range>
        if self.kwargs.get('slug', None):  # for get sub category prouduct
            category_object = Category.objects.get(slug=self.kwargs['slug'])
            final_category_list = category_object.get_all_sub_childrens_
            final_category_list = [*list(final_category_list), category_object]
            qs = Product.objects.filter(category__in=final_category_list).order_by('-publish_time')
            qs_list = []
            for i in qs:
                if i.find_all_size_and_color:
                    qs_list.append(i)
            qsd = sorted(qs_list, key=lambda t: t.first_min_price)
            # print('price', qsd[0].first_min_price)
            if len(qsd) > 0:
                context['first_price_range'] = qsd[0]
                context['last_price_range'] = qsd[-1]
        # < end the price range>
        
        # context['formattrs'] = ProductAttrsForm()


        # <calculate off percent>
        #  context['off_percent_list'] = {}
        #  for current_product in context['object_list']:
        #      if Off.objects.filter(product_id=current_product.id):
        #          product_prcie = ShopProduct.objects.filter(product_id=current_product.id)[0].price
        #          off_price = Off.objects.filter(product_id=current_product.id)[0].price
        #          off_percent = int((product_prcie - off_price)*100/product_prcie)
        #          context['off_percent_list'][current_product.id] = off_percent

        # <end calculate off percent>

        # context["product_images_list"] = Image.objects.filter(product=context['object_list'])
        # context['filter_form'] = forms.FilterListView(self.request.GET)
        # get_copy = self.request.GET.copy()
        # if get_copy.get('page'):
        #     get_copy.pop('page')
        # context['get_copy'] = get_copy
        # print(context['object_list'])

        return context


class ProductDetail(FormMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    form_class = CommentForm
    # success_url = reverse_lazy('detail_product', slug= kwargs['slug'],id= kwargs['id'])

    def get_success_url(self):
        if self.kwargs.get('id_shopprocut'):
            return reverse_lazy ('detail_product', kwargs={'slug':self.kwargs['slug'], 'id':self.kwargs['id_shopprocut']})
        else:
            return reverse_lazy ('detail_product_not_seller', kwargs={'slug':self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['form'] = CommentForm()#initial={'product':self.object}

        context["category_list"] = Category.objects.all()

        # < product image from Image class >
        context['product_image'] = Image.objects.filter(product__slug=self.kwargs['slug'])
        # < end product image from Image class >

        # < current shopProduct >
        if len(self.kwargs) > 1:  # check product does have a shopproduct or not
            context['current_shop_product'] = ShopProduct.objects.filter(id=self.kwargs['id'])
        # < end current shopProduct >

        # < find the shop products for shop >
        if self.request.user.is_authenticated and Shop.objects.filter(user=self.request.user):
            shopproducts = ShopProduct.objects.filter(
                shop=self.request.user.get_shop, 
                product__slug=self.kwargs['slug']
                ).order_by('size','color')
            # print('shopproducts: ', shopproducts)
            context['shopproducts'] = shopproducts
        # < end >

        # < comment >

        # < end comment >


        # < calculate off percent >
        # if Off.objects.filter(product_id=current_product[0].id):
        #     product_price = ShopProduct.objects.filter(product_id=current_product[0].id)
        #     off_price = Off.objects.filter(product_id=current_product[0].id)
        #     off_percent = int((product_price[0].price - off_price[0].price)*100/product_price[0].price)
        #     context['off_percent'] = off_percent
        # <end calculate off percent>
        # pprint(ShopProduct.__dict__)
        return context

    # for posting the comment
    def post(self, request, *args, **kwargs):
        # self.oject = self.get_object()
        form = self.get_form()
        if Comment.objects.filter(product__slug=self.kwargs['slug'], user=self.request.user).exists():
            messages.info(request, 'شما قبلا نظر خود را ثبت کرده اید')
            if self.kwargs.get('id'):
                return redirect ('detail_product', slug=self.kwargs['slug'], id=self.kwargs['id'])
            else:
                return redirect ('detail_product_not_seller', slug=self.kwargs['slug'])
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_valid(form)
        
    
    def form_valid(self, form):
        form.instance.product = Product.objects.get(slug=self.kwargs['slug'])
        form.instance.user = self.request.user
        # if request.user.is_superuser:
        #     form.instance.is_active = True
        form.save()
        return super(ProductDetail, self).form_valid(form)


class ProductListSeller(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product_list_seller.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(ShopProduct__shop__slug=self.kwargs[
            'slug'])  # use category list  to filter get products with slug of curent page
        # print('queryset', queryset)
        product_check_list = []
        for i in queryset:
            if not i.name in product_check_list:
                product_check_list.append(i.name)
        # print('category_check_list', product_check_list)

        # for i in product_check_list:
        #     queryset = queryset.filter(name=i)[1:].delete()
        # print('queryset', queryset)

        brand_filter = self.request.GET.get('brand_filter')  # for filter
        if brand_filter:
            queryset = queryset.filter(brand__name=brand_filter)

        order_by = self.request.GET.get('order_by')  # for sort by date
        if order_by:
            queryset = queryset.order_by(order_by)

        category_filter = self.request.GET.get('category_filter')  # for filter
        if category_filter:
            queryset = queryset.filter(category__slug=category_filter)
        # print('queryset: ', queryset)
        # print('len queryset: ', len(queryset))
        # print("set queryset: ", set(queryset))
        # print("len set queryset: ", len(set(queryset)))
        return set(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('object_list', context['object_list'])
        context['curent_slug_object'] = Shop.objects.filter(slug=self.kwargs['slug'])

        # < find the brand list >
        all_objexts_list = context['object_list']
        cleaned_list = []
        for i in all_objexts_list:
            if i.brand not in cleaned_list:
                cleaned_list.append(i.brand)
        context['brand_list'] = cleaned_list
        # < end find brand list >

        # < entity category list >
        cleaned_list = []
        for i in all_objexts_list:
            if i.category not in cleaned_list:
                cleaned_list.append(i.category)
        context['entity_category_list'] = cleaned_list
        # < end entity category list >

        context["category_list"] = Category.objects.all()
        return context


class SellerShopProduct(LoginRequiredMixin, CreateView):
    form_class = SellerShopProductForm
    template_name = 'shop/create_new_product.html'

    # for auto add the shop field
    def form_valid(self, form):
        form.instance.shop = self.request.user.get_shop
        # print('get kwargs: ', self.kwargs['product'])
        form.instance.product = Product.objects.get(pk=self.kwargs['product'])
        # print('form', form)
        return super(SellerShopProduct, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()

        # print('get kwargs: ', self.kwargs['product'])
        context["product_name"] = Product.objects.get(pk=self.kwargs['product'])
        # print('product_name: ', context['product_name'])
        return context
    
    def get_success_url(self):
        print('created Slug and Id: ', ShopProduct.objects.get(id=self.object.id).product.slug, self.object.id)# self.object.slug ,  self.kwargs['id']
        return reverse_lazy('detail_product', kwargs={'slug': ShopProduct.objects.get(id=self.object.id).product.slug, 'id': self.object.id})
        # if self.kwargs.get('id'):
            # return reverse_lazy(
            #     'detail_product',
            #     kwargs={
            #         'slug':Product.objects.filter(pk=self.kwargs.get['product']).first.slug,
            #         'id':Product.objects.filter(pk=self.kwargs['product']).first.first_min_price.id,
            #     }
            # )
        # else:
        #     return reverse_lazy ('detail_product_not_seller', kwargs={'slug':Product.objects.filter(pk=self.kwargs.get['product']).first.slug})


class SellerEditShopProduct(LoginRequiredMixin, UpdateView):
    form_class = SellerShopProductForm
    # success_url = reverse_lazy('profile')
    template_name = 'shop/edit_product.html'
    # success_message = 'your profile was created successfully'

    #for limited user to access another users profile we can do this or use 'LoginRequiredMixin'
    #now we did not use pk for address the profile page of logined user and did not use pk for url
    def get_object(self, queryset=None):
        return get_object_or_404(
            ShopProduct, 
            shop = Shop.objects.get(user=self.request.user), 
            product = Product.objects.get(id = self.kwargs.get('pk')),
            size = Size.objects.get(name = self.kwargs.get('size')),
            color = Color.objects.get(name = self.kwargs.get('color')),
            )

    # # for auto add the shop field
    # def form_valid(self, form):
    #     form.instance.shop = self.request.user.get_shop
    #     # form.instance.product = Product.objects.get(id=self.kwargs['id'])
    #     # form.instance.size = Size.objects.get(name=self.kwargs['size'])
    #     # form.instance.color = Color.objects.get(name=self.kwargs['color'])
    #     form.save()
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SellerEditShopProduct, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        # print('get kwargs: ', self.kwargs['product'])
        # context["product_name"] = Product.objects.get(id=self.kwargs['id'])
        # context["product_size"] = Size.objects.get(name =self.kwargs['size'])
        # context["product_color"] =  Color.objects.get(name=self.kwargs['color'])
        # print('product_name: ', context['product_name'])
        return context

    def get_success_url(self):
        # if self.kwargs.get('id'):
        return reverse_lazy ('detail_product', kwargs={'slug':self.kwargs['slug'], 'id':self.kwargs['id']})
        # else:
        #     return reverse_lazy ('detail_product_not_seller', kwargs={'slug':self.kwargs['slug']})


def remove_prodcut_from_store(request, slug,pk):
    shopproduct = ShopProduct.objects.get(pk = pk)
    shopproduct.delete()
    #print(basket_item[0].quantity)
    messages.info(request, 'این محصول از فروشگاه شما حذف شد')
    id = Product.objects.get(slug=slug)
    print('id is: ', id)
    # return redirect('search_product_seller')
    print('id is: ', id.first_min_price_)
    if id.first_min_price_id:
        return redirect('detail_product', slug= slug, id=id.first_min_price_id)
    else:
        return redirect('detail_product_not_seller', slug= slug)


def add_to_wish_list(request, slug, id):
    if WishList.objects.filter(user=request.user, product__slug=slug).exists():
        messages.info(request, 'این محصول در لیست علاقه مندی شما وجود دارد!')
    else:
        product = Product.objects.get(slug=slug)
        user = request.user
        wishlist = WishList.objects.create(user=user, product=product)
        messages.info(request, 'این محصول به لیست علاقه مندی شما اضافه شد')
    return redirect('detail_product', slug=slug, id=id)


def add_to_wish_list_without_id(request, slug):
    if WishList.objects.filter(user=request.user, product__slug=slug).exists():
        messages.info(request, 'این محصول در لیست علاقه مندی شما وجود دارد!')
    else:
        product = Product.objects.get(slug=slug)
        user = request.user
        wishlist = WishList.objects.create(user=user, product=product)
        messages.info(request, 'این محصول به لیست علاقه مندی شما اضافه شد')
    return redirect('detail_product_not_seller', slug=slug)


class WishListView(LoginRequiredMixin, ListView):
    model = WishList
    template_name = 'wish_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # print('type wishlist', type(WishList))
        queryset = WishList.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        context['user_name'] = self.request.user.first_name
        # context['wish_list_objects'] = WishList.objects.filter(user=self.request.user)
        return context


def remove_from_wish_list(request, id):
    print(id)
    wish_item = WishList.objects.get(id=id)
    wish_item.delete()
    messages.info(request, 'این محصول از لیست علاقه مندی های شما حذف شد')
    return redirect("wish_list")


class CommentLikeView(View):

    def get_success_url(self):
        print('slug and id:', self.kwargs['slug'], self.kwargs['id'])
        return reverse_lazy ('detail_product', kwargs={'slug':self.kwargs['slug'], 'id':self.kwargs['id']})
    
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = self.request.user
        if not CommentDisLike.objects.filter(user=user, comment=comment):
            like = CommentLike.objects.create(user=user, comment=comment)
            return redirect(self.get_success_url())
        else:
            dislike = CommentDisLike.objects.get(user=user, comment=comment)
            dislike.delete()
            like = CommentLike.objects.create(user=user, comment=comment)
            return redirect(self.get_success_url())


class CommentDisLikeView(View):

    def get_success_url(self):
        print('slug and id:', self.kwargs['slug'], self.kwargs['id'])
        return reverse_lazy ('detail_product', kwargs={'slug':self.kwargs['slug'], 'id':self.kwargs['id']})
    
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = self.request.user
        if not CommentLike.objects.filter(user=user, comment=comment):
            dislike = CommentDisLike.objects.create(user=user, comment=comment)
            return redirect(self.get_success_url())
        else:
            like = CommentLike.objects.get(user=user, comment=comment)
            like.delete()
            dislike = CommentDisLike.objects.create(user=user, comment=comment)
            return redirect(self.get_success_url())


class EditCommentView(LoginRequiredMixin, UpdateView):
    form_class = CommentForm
    template_name = 'edit_comment.html'

    def get_success_url(self):
        if self.kwargs.get('id'):                    
            return reverse_lazy ('detail_product', kwargs={'slug':self.kwargs['slug'], 'id':self.kwargs['id']})
        else:
            return reverse_lazy ('detail_product_not_seller', kwargs={'slug':self.kwargs['slug']})

    #for limited user to access another users profile we can do this or use 'LoginRequiredMixin'
    #now we did not use pk for address the profile page of logined user and did not use pk for url
    def get_object(self, queryset=None):
        return get_object_or_404(
            Comment, 
            product = Product.objects.get(slug = self.kwargs.get('slug')),
            user = self.request.user,
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


