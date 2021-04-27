from django.shortcuts import render

# method index
def index(request):
    context = {
        'judul': 'Home',
        'kontributor': 'Parent dari Home',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ],
        'banner': 'img/banner_home.png'
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
