# Generated by Django 2.2.4 on 2019-09-17 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190916_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Order'),
            preserve_default=False,
        ),
    ]