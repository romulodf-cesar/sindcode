from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
def beneficios(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não logado')
        return redirect('login')
    return render(request, 'beneficios/beneficios.html')