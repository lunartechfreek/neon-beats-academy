from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, ContactUs, FAQ

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the about model.
    """
    summernote_fields = ('about_text',)
    list_display = ('about_text', 'about_image', 'updated_on')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the recieved messages
    from users.
    """
    list_display = ('name', 'email', 'message', 'read')
    list_filter = ('read',)
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Frequently Asked Questions (FAQ).
    """
    list_display = ('question', 'importance', 'created_on', 'updated_on')
    list_filter = ('importance', 'created_on', 'updated_on')
    search_fields = ('question',)
    ordering = ['importance', 'created_on']