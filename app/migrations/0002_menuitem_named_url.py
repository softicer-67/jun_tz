# Generated by Django 5.0.4 on 2024-04-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='named_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
