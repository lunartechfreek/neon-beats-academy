from django.shortcuts import render
from django.contrib import messages
from .models import Newsletter, NewsletterInfo
from .forms import NewsletterForm


def subscribe(request):
    """
    Handle the subscription form and display the latest newsletter information.
    """
    # Handle the subscription form submission
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email is already subscribed
            if Newsletter.objects.filter(email=email).exists():
                messages.error(
                    request, "You are already subscribed to the newsletter!")
            else:
                form.save()
                messages.success(
                    request, "Thank you for subscribing to our newsletter!")
    else:
        form = NewsletterForm()

    # Fetch the latest newsletter information
    newsletter_info = NewsletterInfo.objects.order_by('-updated_on').first()

    # Fallback if no NewsletterInfo entry exists
    if not newsletter_info:
        newsletter_info = NewsletterInfo(
                newsletter_info="No newsletter information available.",
                updated_on="Unknown")

    context = {
        'form': form,
        'newsletter_info': newsletter_info,
    }

    return render(request, 'newsletter/subscribe.html', context)
