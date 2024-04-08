# Generated by Django 5.0.2 on 2024-04-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_image'),
        ('profiles', '0002_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='fav_product', to='catalog.product'),
        ),
    ]
