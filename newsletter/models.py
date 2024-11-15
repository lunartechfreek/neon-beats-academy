from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(unique=True, blank=False)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
