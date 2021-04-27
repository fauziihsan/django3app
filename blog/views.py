from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul': 'Blog',
        'kontributor': 'Fauzi Ihsan',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ]
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