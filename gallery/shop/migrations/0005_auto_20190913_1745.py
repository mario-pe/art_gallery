# Generated by Django 2.2.4 on 2019-09-13 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190913_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='products',
            new_name='product',
        ),
    ]