# Generated by Django 2.2.4 on 2019-09-17 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_product_order_produckt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order_produckt',
        ),
    ]
