from django.urls import path

from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualizar_cliente/', views.atualiza_cliente, name="atualiza_cliente"),
    path('atualizar_carro/<int:id>', views.atualiza_carro, name='atualiza_carro'),
    path('excluir_carro/<int:id>', views.excluir_carro, name='excluir_carro' ),
    
]
