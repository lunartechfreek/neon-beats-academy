from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Newsletter, NewsletterInfo


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)
    fields = ('email',)
    readonly_fields = ('date_subscribed',)


@admin.register(NewsletterInfo)
class NewsletterInfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('newsletter_info',)
    list_display = ('newsletter_info', 'updated_on')
    readonly_fields = ('updated_on',)
