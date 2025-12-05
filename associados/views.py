from django.shortcuts import render, redirect
from associados.forms import AssociadoForm, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def associados(request):
    return render(request, 'associados/index.html')


def login(request):
    form = LoginForms(request.POST)

    # Verificar envio da requisição
    if request.method == 'POST':
        # Se a requisição for POST (tentativa de login)
        nome = form['nome_login'].value()
        senha = form['senha'].value()
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            # Se o usuário for autenticado com sucesso
            auth.login(request, usuario)
            messages.success(request,f'{nome} logado com sucesso!')
            return redirect('beneficios')
        else:
            messages.error(request,'Erro ao efetuar o login!')
            return redirect('login')
        # Se o login falhar (usuario é None), o fluxo continua para a linha
        # que renderiza o formulário com a variável 'form' (que pode ter erros).

    # Se a requisição não for POST (é GET, ou POST falhou)
    return render(request, 'associados/login.html', {'form': form})

def cadastro(request):
    form = AssociadoForm()
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                 messages.error(request,'As senhas não são iguais!')
                 return redirect('cadastro')
            nome_completo = form['nome_completo'].value()
            nome_social = form['nome_social'].value()
            identidade_genero = form['identidade_genero'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            if User.objects.filter(username=nome_completo).exists():
                return redirect('cadastro')
            # criar um novo associado
            associado = User.objects.create_user(
                username = nome_completo,
                email = email,
                password=senha
            )
            associado.save()
            messages.success(request,'Cadastrado efetuado com sucesso!')
            return redirect('login')


    return render(request, 'associados/cadastro.html',{'form': form})

