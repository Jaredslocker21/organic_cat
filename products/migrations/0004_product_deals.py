# Generated by Django 3.2 on 2023-02-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_clearance'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deals',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]