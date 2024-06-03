from django.shortcuts import render
from blog_app.models import Post, Comment

# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog_app/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("created_on")
    context = {
        "category":category,
        "posts": posts,
    }
    return render(request, "blog_app/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context =  {
        "post":post,
        "comments":comments,
    }

    return render(request, "blog_app/detail.html", context)
