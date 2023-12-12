from django.shortcuts import render, redirect

# Import Models
from .models import *


def index(request):
    posts = Post.objects.all()
    categorys = Category.objects.all()
    return render(request, "Index.html", locals())


def upload(request):
    categorys = Category.objects.all()

    if request.method == "POST":
        upload_title = request.POST.get("upload_title")
        upload_description = request.POST.get("upload_description")
        upload_category = request.POST.get("upload_category")
        # Handle Category -----------------------------------------------
        category_instance = Category.objects.get(db_name=upload_category)
        create_post = Post(
            db_title=upload_title,
            db_description=upload_description,
            db_category=category_instance
        )
        create_post.save()
    return render(request, "Upload.html", locals())
