# Generated by Django 3.2.25 on 2024-10-30 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='difficulty',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], help_text='Difficulty level from 1 (easiest) to 10 (most difficult)'),
        ),
    ]
