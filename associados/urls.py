from django.urls import path
from associados.views import associados
urlpatterns = [
    path('associados',associados, name='associados'),

]