# Generated by Django 2.2.4 on 2019-09-12 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_address_cart_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_value',
        ),
    ]