# Generated by Django 3.2.7 on 2021-11-02 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20211102_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminshoppingcart',
            name='userOfShoppingCard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersOfShoppingCard', to='product.shopping_card', verbose_name='user'),
        ),
    ]