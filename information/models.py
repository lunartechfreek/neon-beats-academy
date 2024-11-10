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