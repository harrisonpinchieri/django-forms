from django.urls import path
from .views import index, revisao_consulta

urlpatterns = [
    path('',index, name='index'),
    path('minha_consulta',revisao_consulta,name='minha_consulta')
]