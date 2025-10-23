from django.shortcuts import render

def index(request):
    return render(request, 'associados/index_demo.html')
