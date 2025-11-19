from django.urls import path
from noticias.views import index
from noticias.views import autores
from noticias.views import buscar
from noticias.views import detalhe_noticia

urlpatterns = [
    path("", index, name="index"),
    path('autor/',autores),
    path("buscar",buscar,name="buscar"),
    path('<int:noticia_id>/', detalhe_noticia, name='detalhe_noticia'),
]