from django.shortcuts import render,get_object_or_404
from noticias.models import Categoria, Autor,Noticia
from django.db.models import Q

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request,
                  'noticias/index.html',
                  {'cards':categorias})
def autores(request):
    autores = Autor.objects.all()
    return render(request,'noticias/nossos_autores.html',{'autores':autores})

def index(request):
    noticias = Noticia.objects.all()
    return render(request,'noticias/index.html',{'noticias':noticias})

def buscar(request):
    noticias = Noticia.objects.all()
    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            # 1. Crie as duas condições de busca
            condicao_titulo = Q(titulo__icontains=nome_buscar)
            condicao_conteudo = Q(conteudo__icontains=nome_buscar)

            # 2. Combine as condições usando o operador OU (|)
            filtro_ou = condicao_titulo | condicao_conteudo

            # 3. Aplique o filtro ao seu QuerySet
            noticias = Noticia.objects.filter(filtro_ou)
        else:
            # Se não houver termo de busca, retorne todas as notícias
            noticias = Noticia.objects.all()
    return render(request,'noticias/buscar.html',{'noticias':noticias})

def detalhe_noticia(request, noticia_id):
    noticia_principal = get_object_or_404(Noticia, pk=noticia_id)
    ultimas_noticias = Noticia.objects.exclude(pk=noticia_id).order_by('-data_publicacao')[:4]
    contexto = {
        'noticia': noticia_principal,
        'ultimas_noticias': ultimas_noticias
    }
    return render(request, 'noticias/detalhe_noticia.html', contexto)

def flipbook_view(request):
    # Lista simples das páginas (para referência no template)
    # Na vida real, isso viria de um modelo do Django (e.g., Catálogo.objects.all())
    context = {
        'pages_count': 3, # Exemplo: temos 3 páginas (p1.jpg, p2.jpg, p3.jpg)
    }
    return render(request, 'noticias/flipbook.html', context)
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



