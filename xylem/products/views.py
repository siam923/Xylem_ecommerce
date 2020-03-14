# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Product, Review, Category, CategoryImage

from users.models import VendorProfile

from .filters import ProductFilter #CategoryProductFilter


class ProductListView(ListView): # Used for searching also
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['query'] = self.request.GET.get('name')
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'price', 'product_cover',
                'featured', 'active', 'description', 'category',
                'on_sale', 'sale_price', 'sku')
    success_url = reverse_lazy('product_list')
    template_name = 'products/product_create.html'

    def form_valid(self, form):
        user = self.request.user
        vendor = VendorProfile.objects.get(user=user.pk)
        form.instance.vendor = vendor
        return super().form_valid(form)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    success_url = reverse_lazy('product_list')
    fields = ('review',)
    template_name = 'products/review_create.html'

    def form_valid(self, form, *args, **kwargs):
        pid = self.kwargs['pk']
        user = self.request.user
        product = Product.objects.get(id=pid)
        form.instance.product = product
        form.instance.user = user
        return super().form_valid(form)

class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'products/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'products/category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        id = self.get_object()
        context['products'] = Product.objects.filter(category=id)
        context['banners'] = CategoryImage.objects.filter(category=id)[0]
        # context['filter'] = CategoryProductFilter(self.request.GET, queryset=self.get_queryset())
        return context
