from django.urls import path
from noticias.views import index
from noticias.views import autores

urlpatterns = [
    path('',index),
    path('autor/',autores),
]