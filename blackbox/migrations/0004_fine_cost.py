# Generated by Django 3.0.6 on 2020-05-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackbox', '0003_fine_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine',
            name='cost',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
