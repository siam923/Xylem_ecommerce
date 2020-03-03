from django.urls import path

from .views import VendorCreateView, ProfileView


urlpatterns = [
    path('vendor/create', VendorCreateView.as_view(), name='vendor_create'),
    path('<int:pk>/', ProfileView.as_view(), name='profile_detail'),
]
