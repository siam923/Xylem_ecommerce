from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User Management
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('users.urls')),

    # Local apps
    path('', include('pages.urls')),
    path('products/', include('products.urls')),

]
