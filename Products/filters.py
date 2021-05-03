from .models import Product, Category, Brand, ShopProduct
import django_filters
from django import forms


# class CustomFilterSet(django_filters.FilterSet):
#     @classmethod
#     def get_fields(cls):
#         fields = super().get_fields()
#         for name, lookups in fields.items():
#             if name=="name":
#                 lookups[:] = ['icontains']
#         return fields


class ProductListFilter(django_filters.FilterSet):

    name= django_filters.CharFilter(lookup_expr="icontains")
    # brand = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple)
    # name= django_filters.CharFilter(lookup_expr="exact")
    # modifie the 'name' field in hear

    price_order = django_filters.ModelMultipleChoiceFilter(
        queryset=ShopProduct.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
    )


    # # can add some extra field
    # first_name = django_filters.CharFilter(lookup_expr="icontains")
    # # any 'first_name' contain that characters we define
    # year_joined = django_filters.NumberFilter('date_joined', lookup_expr='year')
    # # search for year. the first argoman is the name of field and should be: [
    # # date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, 
    # # last_login, last_name, logentry, password, post, user_permissions, username]
    # # the lookup is should be the: [year, month, day]
    # year_joined__gt = django_filters.NumberFilter('date_joined', lookup_expr='year__gt')
    # # gt means: greater than
    # year_joined__lt = django_filters.NumberFilter('date_joined', lookup_expr='year__lt')
    # # lt means: less than
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)

    # CHOICES = (
    #     ('alphabet', 'Alphabet'),
    #     ('reverseAlphabet', 'reverseAlphabet'),
    # )
    # ordering = django_filters.ChoiceFilter(label='Ordering by username', choices=CHOICES, method='filter_by_order')

    # def __init__(self, category, *args, **kwargs):
    #     super(ProductListFilter, self).__init__(*args, **kwargs)
    #     # choices = self.fields['subcategory'].extra['choices']
    #     # choices += [
    #     #     (subcat.name, subcat.name) for subcat 
    #     #     in SubCategory.objects.filter(category=category)
    #     # ]

    class Meta:
        model = Product
        fields = ['name', 'brand']# brand
        # fields = {
        #     "name":['icontains', ],
        #     # "brand":[]
        # }
        # fields = {
        #     'username': ['exact', ],
        #     'first_name': ['icontains', ],
        #     'last_name': ['exact', ],
        #     'date_joined': ['year', 'year__gt', 'year__lt', 'month', 'month__lt', 'day'],
        # }
        # another option for the manul defind is define the dictionary

    # def filter_by_order(self, queryset, name, value):
    #     expression = 'username' if value=='alphabet' else '-username'
    #     return queryset.order_by(expression)

    # @property
    # def qs(self):
    #     queryset = super(ProductListFilter, self).qs
    #     # current_category = self.request.GET.get('category_slug')
    #     # if current_category:
    #     #     logger.info("Current category is in url")
    #     #     return queryset.filter(category__slug=current_category)
    #     return queryset