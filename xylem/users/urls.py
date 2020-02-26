from django.urls import include, path

from .views import (CustomerSignUpView, VendorSignUpView, SuccessView)


urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/customer', CustomerSignUpView.as_view(), name='signup_customer'),
    path('signup/vendor', VendorSignUpView.as_view(), name='signup_vendor'),
    path('signup/success', SuccessView.as_view(), name='signup_success')
]
