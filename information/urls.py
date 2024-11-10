from . import views
from django.urls import path

# Url patterns for the information app
urlpatterns = [
    path('about/', views.about_us, name='about'),
]