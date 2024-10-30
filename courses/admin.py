from django.contrib import admin
from .models import Course, CourseTier

class CourseAdmin(admin.ModelAdmin):
    exclude = ('sku',)  # Exclude SKU from the admin form

admin.site.register(Course)
admin.site.register(CourseTier)