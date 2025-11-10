from django.urls import path
from noticias.views import index
from noticias.views import autores
from noticias.views import noticias_em_destaque
urlpatterns = [
    path('',index),
    path('autor/',autores),
    path('noticias/',noticias_em_destaque)
]