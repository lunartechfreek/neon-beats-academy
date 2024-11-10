from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the about model.
    """
    list_display = ('about_text', 'about_image', 'updated_on')
