# Generated by Django 3.2.25 on 2024-11-17 13:14

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20241107_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
