from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.funcao_formulario, name='Formulario'),
    path('pessoas/',views.listar_pessoas, name='Pessoas'),
    path('ver_pessoa/<int:id_pessoa>', views.ver_pessoas, name='Pessoa'),
    path('deletar_pessoa/<int:id_pessoa>', views.deletar_pessoas, name='Deletar')
]