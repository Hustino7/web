# Generated by Django 5.0.1 on 2024-01-31 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
