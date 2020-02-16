from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # User Management
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),

    # Local apps
    path('', include('pages.urls')),

]
