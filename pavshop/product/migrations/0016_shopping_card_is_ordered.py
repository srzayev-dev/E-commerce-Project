# Generated by Django 3.2.7 on 2021-11-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_card',
            name='is_ordered',
            field=models.BooleanField(default=False, verbose_name='Is Main?'),
        ),
    ]
