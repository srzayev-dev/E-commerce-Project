# Generated by Django 3.2.7 on 2021-11-02 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_iteminshoppingcart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminshoppingcart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prd', to='product.product', verbose_name='Product'),
        ),
    ]
