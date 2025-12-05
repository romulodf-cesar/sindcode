from django.shortcuts import render

def beneficios(request):
    return render(request, 'beneficios/beneficios.html')