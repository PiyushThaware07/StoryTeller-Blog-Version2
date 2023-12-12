from django.db import models

class Category(models.Model):
    db_id = models.AutoField(primary_key=True)
    db_name = models.CharField(max_length=255, blank=False)

class Post(models.Model):
    db_id = models.AutoField(primary_key=True)
    db_title = models.CharField(max_length=255, blank=False)
    db_description = models.TextField(blank=False)
    db_publish = models.DateField(auto_now=True)
    db_category = models.ForeignKey(Category, on_delete=models.CASCADE)
