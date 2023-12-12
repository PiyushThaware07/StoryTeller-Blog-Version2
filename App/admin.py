from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ["db_id", "db_title", "db_publish", "db_category"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
