from django.urls import path

from .views import (ProductListView, ProductDetailView,
                    ProductCreateView, ReviewCreateView)
from cart.views import add_to_cart, remove_from_cart, CartView, decreaseCart


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductCreateView.as_view(), name='product_create'),
    path('<uuid:pk>/review/add/', ReviewCreateView.as_view(), name='review_create'),

    ## Cart urls
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
]
