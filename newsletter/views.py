from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib import messages
from .models import Newsletter, NewsletterInfo
from .forms import NewsletterForm


def _send_subscribe_email(request, email):
    """Send the user a subscribe email."""
    try:
        subject = render_to_string(
            'newsletter/subscribe_emails/subscribe_email_subject.txt'
        ).strip()

        body = render_to_string(
            'newsletter/subscribe_emails/subscribe_email_body.txt',
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )
    except Exception:
        messages.error(request, "There was an issue sending the confirmation \
        email. Please try again later.")


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
                _send_subscribe_email(request, email)
    else:
        form = NewsletterForm()

    newsletter_info = NewsletterInfo.objects.order_by('-updated_on').first()

    # Fallback if no NewsletterInfo entry exists
    if not newsletter_info:
        newsletter_info = NewsletterInfo(
            newsletter_info="No newsletter information available.",
            updated_on="Unknown"
        )

    context = {
        'form': form,
        'newsletter_info': newsletter_info,
    }

    return render(request, 'newsletter/subscribe.html', context)
