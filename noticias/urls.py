from django.urls import path
from noticias.views import index

urlpatterns = [
    path('',index),
]