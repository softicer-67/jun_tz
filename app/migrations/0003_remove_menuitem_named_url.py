# Generated by Django 5.0.4 on 2024-04-09 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_menuitem_named_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='named_url',
        ),
    ]
