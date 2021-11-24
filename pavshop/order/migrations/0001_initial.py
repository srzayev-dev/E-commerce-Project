# Generated by Django 3.2.7 on 2021-10-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout_billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('town', models.CharField(max_length=255, verbose_name='Town')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Checkout_billing',
                'verbose_name_plural': 'Checkout_billings',
            },
        ),
        migrations.CreateModel(
            name='Payment_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment', models.IntegerField(default=1, verbose_name='Payment')),
            ],
            options={
                'verbose_name': 'Payment_method',
                'verbose_name_plural': 'Payment_methods',
            },
        ),
        migrations.CreateModel(
            name='Shipping_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('town', models.CharField(max_length=255, verbose_name='Town')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('is_main', models.BooleanField(default=False, verbose_name='Is Main?')),
            ],
            options={
                'verbose_name': 'Shipping_Info',
                'verbose_name_plural': 'Shipping_Infos',
            },
        ),
    ]
