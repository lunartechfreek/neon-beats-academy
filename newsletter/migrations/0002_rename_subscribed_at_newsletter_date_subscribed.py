# Generated by Django 3.2.25 on 2024-11-15 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='subscribed_at',
            new_name='date_subscribed',
        ),
    ]
