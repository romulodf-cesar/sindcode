from django.shortcuts import render
from django.http import HttpResponse

# função
# se def dentro classe = metodo
# se def fora classe = função
def index(request):
    #return HttpResponse("<h1>Alô Django 2025</h1>")
    return render(request, 'noticias/index.html')