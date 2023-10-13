from django.urls import path
from agendaFinanceira import views
from agendaFinanceira.models import Fornecedor
from django_select2.views import AutoResponseView
from .views import  cadastrar_despesa, cadastrar_fornecedor, cadastrar_contasapagar, cadastrar_cliente, cliente_list, fornecedor_list, despesa_list, saldoinicial, saldoatual, update_saldo_atual, saldoatual_list

urlpatterns = [
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('cadastrar_receita/', views.cadastrar_receita, name='cadastrar_receita'),
    path('receita_list/', views.receita_list, name='receita_list'),
    path('cadastrar_despesa/', views.cadastrar_despesa, name='cadastrar_despesa'),
    path('despesa_list/', views.despesa_list, name='despesa_list'),
    path('cadastrar_fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedor_list/', views.fornecedor_list, name='fornecedor_list'),
    path('cadastrar_contasapagar/', views.cadastrar_contasapagar, name='cadastrar_contasapagar'),
    path('cadastro_saldoinicial/', views.saldoinicial, name='cadastro_saldoinicial'),
    path('saldoatual/', views.saldoatual, name='saldoatual'),
    path('atualiza_saldoatual/<int:pk>/', views.update_saldo_atual, name='atualiza_saldoatual'),
    path('saldoatual_list/', views.saldoatual_list, name='saldoatual_list'),

    # Adicione outras URLs conforme necessário
]
