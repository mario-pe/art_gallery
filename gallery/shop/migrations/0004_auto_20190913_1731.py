# Generated by Django 2.2.4 on 2019-09-13 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_cart_cart_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='product_value',
        ),
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Client'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.OrderProduct'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Order'),
        ),
    ]