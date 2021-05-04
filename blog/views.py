from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    #  Queryset
    posts = Post.objects.all()
    context = {
        'judul': 'Blog',
        'kontributor': 'Parent dari Blog',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ],
        'banner': 'blog/img/banner_blog.png',
        'app_css': 'blog/css/styles.css',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul': 'Cerita',
        'kontributor': 'Fauzi Cerita'
    }
    return render(request, 'blog/blog.html', context)

def news(request):
    context = {
        'judul': 'News',
        'kontributor': 'Fauzi News'
    }
    return render(request, 'blog/blog.html', context)