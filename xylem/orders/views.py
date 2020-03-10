from django.shortcuts import render
from django.views.generic.base import TemplateView
import stripe
from django.conf import settings


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase one product',
            source=request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')
