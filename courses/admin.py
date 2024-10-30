from django.contrib import admin
from .models import Course, CourseTier

class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'tier',
        'price',
        'image',
    )

    ordering = ('sku',)
    exclude = ('sku',)  # Exclude SKU from the admin form

class CourseTierAdmin(admin.ModelAdmin):
    list_display = (
        'tier_name',
        'has_description'
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTier, CourseTierAdmin)