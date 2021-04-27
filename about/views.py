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
        'banner': 'about/img/banner_about.png',
        'app_css': 'about/css/styles.css'
    }
    return render(request, 'index.html', context)