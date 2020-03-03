from django.urls import path

from .views import (ProductListView, ProductDetailView,
                    ProductCreateView, ReviewCreateView)


urlpatterns = [
path('', ProductListView.as_view(), name='product_list'),
path('<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
path('add/', ProductCreateView.as_view(), name='product_create'),
path('<uuid:pk>/review/add/', ReviewCreateView.as_view(), name='review_create')
]
