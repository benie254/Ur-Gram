# Generated by Django 4.0.4 on 2022-06-08 01:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]