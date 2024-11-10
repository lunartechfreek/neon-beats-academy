from django.shortcuts import render
from .models import About

def about_us(request):
    """Display the 'About' information with text, image, and updated date."""
    about_info = About.objects.first()  # Fetch the first (or only) About entry

    # Fallback for if no About entry exists
    if not about_info:
        about_info = About(about_text="No information available.", updated_on="Unknown")

    context = {
        'about_info': about_info
    }

    return render(request, 'information/about.html', context)
