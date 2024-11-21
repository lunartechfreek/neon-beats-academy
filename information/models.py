from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    A model for the about information.
    """
    about_text = models.TextField()
    about_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Information (Last updated on {self.updated_on})"

    class Meta:
        verbose_name_plural = "About"


class ContactUs(models.Model):
    """
    A model for the contact us form.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Enquiry sent from {self.name}"

    class Meta:
        verbose_name_plural = "Contact Us"


class FAQ(models.Model):
    """
    A model for Frequently Asked Questions.
    """
    question = models.CharField(max_length=500, blank=False, null=False)
    answer = models.TextField(blank=False, null=False)
    importance = models.PositiveIntegerField(
        default=1,
        help_text="Lower values indicate higher importance."
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['importance', 'created_on']
