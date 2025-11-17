from django.urls import path
from noticias.views import index
from noticias.views import autores
from noticias.views import buscar

urlpatterns = [
    path('',index),
    path('autor/',autores),
    path("buscar",buscar,name="buscar"),
]