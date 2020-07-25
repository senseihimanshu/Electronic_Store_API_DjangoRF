# Generated by Django 3.0.8 on 2020-07-25 14:14

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.upload_product_image)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
