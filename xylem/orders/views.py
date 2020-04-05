from django.shortcuts import render
from django.views.generic.base import TemplateView
import stripe
from django.conf import settings
from cart.models import Cart, Order

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(user=self.request.user, ordered=False)
        context['order'] = orders[0]
        context['charge'] = orders[0].get_totals() * 100
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        orders = Order.objects.filter(user=request.user, ordered=False)
        bill = orders[0].get_totals() * 100
        charge = stripe.Charge.create(
            amount= int(bill),
            currency='usd',
            description='Purchase all products',
            source=request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')
