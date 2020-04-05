from django.views.generic import TemplateView
from products.models import Product

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['sale'] = Product.objects.filter(on_sale=True)[:4]
        context['featured'] = Product.objects.filter(on_sale=True)[:6]
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'


