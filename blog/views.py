from django.shortcuts import render

# Create your views here.

def index(request):
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
        'app_css': 'blog/css/styles.css'
    }
    return render(request, 'index.html', context)

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