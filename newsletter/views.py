from django.shortcuts import render
from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if email already exists in the database
            if Newsletter.objects.filter(email=email).exists():
                messages.error(request, "You are already subscribed to the newsletter!")
            else:
                form.save()
                messages.success(request, "Thank you for subscribing to our newsletter!")
    else:
        form = NewsletterForm()

    return render(request, 'newsletter/subscribe.html', {'form': form})
