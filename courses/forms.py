from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from .models import Course, CourseTier


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            # Use Summernote for the description field
            'description': SummernoteWidget(),
        }

    image = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tiers = CourseTier.objects.all()
        tier_names = [(t.id, t.tier_name) for t in tiers]

        self.fields['tier'].choices = tier_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black new-image rounded-0'
