from django.shortcuts import render
from associados.forms import AssociadoForm
def associados(request):
    return render(request, 'associados/index.html')
def login(request):
    return render(request, 'associados/login.html')
def cadastro(request):
    form = AssociadoForm()
    return render(request, 'associados/cadastro.html',{'form': form})