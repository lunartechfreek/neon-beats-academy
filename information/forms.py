from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """
    A form for contacting the site owner
    """
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }