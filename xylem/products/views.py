# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Product, Review

from users.models import VendorProfile

class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'price', 'product_cover', 'featured', 'active', 'category')
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
