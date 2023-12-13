from django.shortcuts import render, redirect,get_object_or_404

# Import Models
from .models import *


def index(request):
    posts = Post.objects.all()
    categorys = Category.objects.all()
    return render(request, "Index.html", locals())

def category(request,category_id):
    categorys = Category.objects.all()
    # Category Banner ------------------
    filter_category = get_object_or_404(Category, db_id=category_id)
    # Category Posts
    category_posts = Post.objects.filter(db_category=filter_category)
    print("Posts ----->> ",category_posts)
    return render(request,"Index.html",locals())


def post(request,post_id):
    return render(request,"Index.html",locals())