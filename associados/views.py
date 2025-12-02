from django.shortcuts import render, redirect
from associados.forms import AssociadoForm, LoginForms


def associados(request):
    return render(request, 'associados/index.html')
def login(request):
    form = LoginForms()
    return render(request, 'associados/login.html', {'form': form})
def cadastro(request):
    form = AssociadoForm()
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form['senha_1'].value() != form['senha_2'].value():
            return redirect('cadastro')
    return render(request, 'associados/cadastro.html',{'form': form})