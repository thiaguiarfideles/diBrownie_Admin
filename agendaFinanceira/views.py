import datetime 
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from usuarios.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from .forms import  ClienteForm, FornecedorForm, ReceitaForm, DespesaForm, LancamentoContasPagarForm
from .models import Cliente, Fornecedor, LancamentoContasPagar, Receita, Despesa
from .serializers import DespesaSerializer, ReceitaSerializer, ClienteSerializer
from dal import autocomplete
import datetime




# Create your views here.

# Pagina inicial
def index(request):
	return render(request, 'agendaFinanceira/index.html', {})

# Cadastrar Usuario

# Logout
def sair(request):
	logout(request)
	return redirect('/')

# -----views com obrigatoriedade de login-----
	
# Menu inical apos login
@login_required
def menu(request):
	return render(request, 'agendaFinanceira/menu.html', {})



def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar Receita. Verifique os campos.')
    else:
        form = ReceitaForm()

    return render(request, 'agendaFinanceiraApp/cadastroReceita.html', {'form': form})

# Visualização para detalhar, atualizar e excluir receitas
class ReceitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    
def cadastrar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'despesa cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar despesa. Verifique os campos.')
    else:
        form = DespesaForm()

    return render(request, 'agendaFinanceiraApp/lancamento_despesa.html', {'form': form})


class FornecedorAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Seu código para obter a lista de fornecedores aqui
        queryset = Fornecedor.objects.all()

        if self.q:
            queryset = queryset.filter(nome__icontains=self.q)

        return queryset


@login_required  # Ensure that the user is logged in to access this view
def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            # Associate the logged-in user with the 'usuario' field before saving
            fornecedor = form.save(commit=False)
            fornecedor.usuario = request.user  # Assign the logged-in user to the 'usuario' field
            fornecedor.save()
            messages.success(request, 'Fornecedor cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar Fornecedor. Verifique os campos.')
    else:
        form = FornecedorForm()

    return render(request, 'agendaFinanceiraApp/cadastroFornecedor.html', {'form': form})

def cadastrar_contasapagar(request):
    if request.method == 'POST':
        form = LancamentoContasPagarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contas a pagar cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar Contas a pagar. Verifique os campos.')
    else:
        form = LancamentoContasPagarForm()

    return render(request, 'agendaFinanceiraApp/lancamento_fornecedor.html', {'form': form})


# Visualização para listar e criar despesas
@login_required  # Ensure that the user is logged in to access this view
def cadastrar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            # Associate the logged-in user with the 'usuario' field before saving
            despesa = form.save(commit=False)
            despesa.usuario = request.user  # Assign the logged-in user to the 'usuario' field
            despesa.save()
            messages.success(request, 'Despesa cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar Despesa. Verifique os campos.')
    else:
        form = DespesaForm()

    return render(request, 'agendaFinanceiraApp/cadastroDespesa.html', {'form': form})

# Visualização para listar e criar despesas
@login_required  # Ensure that the user is logged in to access this view
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Associate the logged-in user with the 'usuario' field before saving
            cliente = form.save(commit=False)
            cliente.usuario = request.user  # Assign the logged-in user to the 'usuario' field
            cliente.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar cliente. Verifique os campos.')
    else:
        form = ClienteForm()

    return render(request, 'agendaFinanceiraApp/cadastroCliente.html', {'form': form})

#@authentication_classes([TokenAuthentication])
##class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Cliente.objects.all()
    #serializer_class = ClienteSerializer
    
def cliente_list(request):
    usuario = request.user
    cadastros = Cliente.objects.filter(usuario=usuario.id)
    return render(request, 'cliente_list.html', {
        'cadastros': cadastros
    })

def fornecedor_list(request):
    usuario = request.user
    cadastros = Fornecedor.objects.filter(usuario=usuario.id)
    return render(request, 'fornecedor_list.html', {
        'cadastros': cadastros
    })
    
def despesa_list(request):
    usuario = request.user
    cadastros = Despesa.objects.filter(usuario=usuario.id)
    return render(request, 'despesa_list.html', {
        'cadastros': cadastros
    })        

# Visualização para detalhar, atualizar e excluir despesas
#class DespesaDetailView(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Despesa.objects.all()
    #serializer_class = DespesaSerializer
    


class ListarLancamentosView(ListView):
    model = LancamentoContasPagar
    template_name = 'view_apagar.html'
    context_object_name = 'lancamentos'
    
    


