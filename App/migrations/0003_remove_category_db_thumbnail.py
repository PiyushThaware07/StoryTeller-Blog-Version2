# Generated by Django 5.0 on 2023-12-13 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_category_db_thumbnail_post_db_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='db_thumbnail',
        ),
    ]
