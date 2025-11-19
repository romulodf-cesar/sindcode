from django.shortcuts import render

def associados(request):
    return render(request, 'associados/index.html')
