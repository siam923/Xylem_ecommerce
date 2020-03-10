## Resource: https://www.youtube.com/watch?v=nle3u6Ww6Xk

import django_filters
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Search')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Min')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Max')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Category')
    on_sale = django_filters.BooleanFilter(field_name='on_sale', label="Sale Products")
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['lt', 'gt'],
            'category': [],
            'on_sale': [],
        }


# class CategoryProductFilter(django_filters.FilterSet):
#     price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Min')
#     price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Max')
#     on_sale = django_filters.BooleanFilter(label="Sale Products")
#     class Meta:
#         model = Product
#         fields = {
#             'price': ['lt', 'gt'],
#             'on_sale': [],
#         }
#
#     @property
#     def qs(self):
#         id = self.kwargs['pk']
#         return Product.objects.filter(category=id)
