from django.db import models
# FILE SYSTEM STORAGE
from django.conf import settings
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Category(models.Model):
    db_id = models.AutoField(primary_key=True)
    db_name = models.CharField(max_length=255, blank=False)
    db_thumbnail = models.ImageField(
        storage=fs, upload_to="category_thumbnails/")


class Post(models.Model):
    db_id = models.AutoField(primary_key=True)
    db_title = models.CharField(max_length=255, blank=False)
    db_description = models.TextField(blank=False)
    db_publish = models.DateField(auto_now=True)
    db_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    db_thumbnail = models.ImageField(storage=fs, upload_to="post_thumbnails/")

