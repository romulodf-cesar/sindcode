from django.urls import path
from noticias.views import noticias
from noticias.views import autores
from noticias.views import buscar

urlpatterns = [
    path('',noticias,name='noticias'),
    path('autor/',autores),
    path("buscar",buscar,name="buscar"),
]