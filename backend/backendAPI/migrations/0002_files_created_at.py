# Generated by Django 4.1.5 on 2023-01-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
