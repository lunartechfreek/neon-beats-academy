from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import ContactUsForm

def about_us(request):
    """
    Display the 'About' information with text, image, and updated date.
    """
    about_info = About.objects.first()  # Fetch the first (or only) About entry

    # Fallback for if no About entry exists
    if not about_info:
        about_info = About(about_text="No information available.", updated_on="Unknown")

    context = {
        'about_info': about_info
    }

    return render(request, 'information/about.html', context)


def contact_us(request):
    """
    Handles the contact form submission.
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!'
                )
            return redirect('contact_us')
        else:
            messages.error(request, 'There was an error with your enquiry. Please check the form and try again.')
    else:
        form = ContactUsForm()

    return render(request, 'information/contact_us.html', {'form': form})