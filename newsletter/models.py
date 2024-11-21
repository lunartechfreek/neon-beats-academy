from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(unique=True, blank=False)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'


class NewsletterInfo(models.Model):
    newsletter_info = models.TextField(unique=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Newsletter Info (Updated on {self.updated_on:%Y-%m-%d %H:%M})"

    class Meta:
        verbose_name = "Newsletter Information"
        verbose_name_plural = "Newsletter Information"
