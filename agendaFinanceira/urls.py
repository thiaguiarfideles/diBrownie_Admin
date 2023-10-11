from django.urls import path
from agendaFinanceira import views
from agendaFinanceira.models import Fornecedor
from django_select2.views import AutoResponseView
from .views import  FornecedorAutocompleteView, ReceitaDetailView, ListarLancamentosView, cadastrar_despesa, cadastrar_fornecedor, cadastrar_contasapagar,cadastrar_cliente,cliente_list,fornecedor_list,despesa_list


urlpatterns = [
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('cadastrar_receita/', views.cadastrar_receita, name='cadastrar_receita'),
    path('receitas_detalhe/<int:pk>/', ReceitaDetailView.as_view(), name='receita-detail'),
    path('listar_lancamentos/', ListarLancamentosView.as_view(), name='listar_lancamentos'),
    path('cadastrar_despesa/', views.cadastrar_despesa, name='cadastrar_despesa'),
    path('despesa_list/', views.despesa_list, name='despesa_list'),
    #path('despesas_detalhe/<int:pk>/', DespesaDetailView.as_view(), name='despesa-detail'),
    path('fornecedor_autocomplete/', FornecedorAutocompleteView.as_view(), name='fornecedor-autocomplete'),
    path('cadastrar_fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedor_list/', views.fornecedor_list, name='fornecedor_list'),
    path('cadastrar_contasapagar/', views.cadastrar_contasapagar, name='cadastrar_contasapagar'),
    # Adicione outras URLs conforme necessário
]
