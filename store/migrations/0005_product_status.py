# Generated by Django 4.2.5 on 2024-02-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(default='In Stock', max_length=20),
        ),
    ]
