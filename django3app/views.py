from django.shortcuts import render

# method index
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
