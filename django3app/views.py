from django.http import HttpResponse

# method index
def index(request):
    judul = '<h1>Hello World!</h1>'
    subjudul = '<h2> Selamat datang di django3app</h2>'
    output = judul + subjudul
    return HttpResponse(output)

def about(request):
    return HttpResponse('<h1>Ini method about</h1>')
