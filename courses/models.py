from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.db import models

class CourseTier(models.Model):
    tier_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tier_name

    # Returns if a description exists or not for the admin panel
    def has_description(self):
        return bool(self.description)  

class Course(models.Model):
    # Tier choices for SKU
    TIER_CHOICES = [
        ('BEG', 'Beginner'),
        ('ADV', 'Advanced'),
        ('CRE', 'Creative'),
        ('COM', 'Complete'),
    ]

    DIFFICULTY_CHOICES = [(i, str(i)) for i in range(1, 11)]  # Dropdown choices for difficulty

    tier = models.ForeignKey('CourseTier', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=20, unique=True, editable=False)
    name = models.CharField(max_length=254, unique=True, blank=False)
    description = models.TextField(blank=False)
    difficulty = models.IntegerField(
        choices=DIFFICULTY_CHOICES,
        help_text="Difficulty level from 1 (easiest) to 10 (most difficult)"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')

    # Generate sku code dynamically
    def save(self, *args, **kwargs):
        if not self.sku:
            tier_code = self.tier.tier_name[:3].upper() if self.tier else 'GEN'
            number = Course.objects.filter(sku__startswith=f'DJ-{tier_code}-').count() + 1  # Count existing SKUs
            self.sku = f'DJ-{tier_code}-{str(number).zfill(3)}'  # Format the number with leading zeros
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['difficulty']

