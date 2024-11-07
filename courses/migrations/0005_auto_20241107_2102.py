# Generated by Django 3.2.25 on 2024-11-07 21:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
