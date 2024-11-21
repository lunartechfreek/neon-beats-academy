from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course, CourseTier


class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

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
