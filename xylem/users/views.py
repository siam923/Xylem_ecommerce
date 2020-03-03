from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import VendorProfile
from users.models import CustomUser, VendorProfile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class VendorCreateView(LoginRequiredMixin, CreateView):
    model = VendorProfile
    template_name = 'users/vendor_create.html'
    fields = ('brand', 'info',)
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        user_info = CustomUser.objects.get(id=user.id)
        user_info.is_vendor = True
        user_info.save()
        form.instance.user = user
        return super().form_valid(form)

# class VendorDetailView(DetailView):
#     model = VendorProfile
#     template_name = 'users/vendor_detail.html'



class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'custom_user'
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        flag = user.is_vendor
        context['flag'] = flag
        if flag:
            vendor = VendorProfile.objects.get(user=user.pk)
            context['brand_name'] = vendor.brand
            context['brand_info'] = vendor.info
        return context
