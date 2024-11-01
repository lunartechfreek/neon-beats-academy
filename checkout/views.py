from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    # Stops users from accessing checkout with an empty bag
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QAdemG1uQMioJNmPF83UTxRDzEx6CoF6Q6MMwrMfFrbaQpwhJE9mEhDZVFGTN1gyDUxjQOy4IeHHqof33NjK0mk00JkYROeA4',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)