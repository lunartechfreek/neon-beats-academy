from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class CourseTier(models.Model):
    tier_name = models.CharField(max_length=100, unique=True)
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Difficulty level from 1 (easiest) to 10 (most difficult)"
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    tier = models.ForeignKey('CourseTier', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

