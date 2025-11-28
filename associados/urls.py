from django.urls import path
from associados.views import associados,login,cadastro
urlpatterns = [
    path('associados',associados, name='associados'),
    path('login',login, name='login'),
    path('cadastro',cadastro, name='cadastro'),

]
