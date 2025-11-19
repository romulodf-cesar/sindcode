from django.shortcuts import render
from noticias.models import Categoria, Autor,Noticia

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request,
                  'noticias/index.html',
                  {'cards':categorias})
def autores(request):
    autores = Autor.objects.all()
    return render(request,'noticias/nossos_autores.html',{'autores':autores})

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request,'noticias/index.html',{'noticias':noticias})

def buscar(request):
    noticias = Noticia.objects.all()
    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            noticias = noticias.filter(conteudo__icontains=nome_buscar)
    return render(request,'noticias/buscar.html',{'noticias':noticias})


"""
def noticias_em_destaque(request):
    # 1. Consulta: Filtra notícias onde 'destaque' é igual a '5'
    # 2. Ordenação: Ordena pelo campo 'data_publicacao' de forma decrescente (mais recente primeiro)
    noticias = Noticia.objects.filter(destaque='5').order_by('-data_publicacao')

    return render(
        request,
        'noticias/destaques.html',
        {'noticias_destaques': noticias}  # Passa as notícias para o template
    )


"""

# função
# se def dentro classe = metodo
# se def fora classe = função

"""
  #return HttpResponse("<h1>Alô Django 2025</h1>")

    # definindo um mock com dict
 
     dados ={
       1:{"titulo":"mulheres dev",
          "conteudo":"mulheres programadores em python",
          "data_publicacao":"29/10/2025"},
       2:{"titulo":"programadores kids",
          "conteudo":"programadores em python no dia das crianças",
          "data_publicacao":"12/10/2025"},
        3: {"titulo": "Josias novo presidente",
            "conteudo": "Josias é nosso novo presidente, um homem de grande sonhos",
            "data_publicacao": "12/10/2025"},
    }
"""

