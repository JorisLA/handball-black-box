# Generated by Django 3.0.6 on 2020-05-09 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blackbox', '0005_userfinehistoric'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfinehistoric',
            name='users',
        ),
        migrations.AddField(
            model_name='userfinehistoric',
            name='users',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
