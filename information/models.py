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