from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'About',
        'kontributor': 'Parent dari About',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ],
        'banner': 'about/img/banner_about.png'
    }
    return render(request, 'about/about.html', context)