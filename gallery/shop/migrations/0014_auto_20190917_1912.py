# Generated by Django 2.2.4 on 2019-09-17 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20190917_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='orders',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Address'),
        ),
    ]
