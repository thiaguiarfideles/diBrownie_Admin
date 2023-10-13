import datetime 
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
#from isoduration import format_duration
from usuarios.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Cliente, Fornecedor, LancamentoContasPagar, Receita, Despesa, SaldoAtual
from agendaFinanceira.forms import ( ClienteForm, FornecedorForm, ReceitaForm, DespesaForm, LancamentoContasPagarForm, SaldoAtlForm, SaldoForm)
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



@login_required  # Ensure that the user is logged in to access this view
def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            # Associate the logged-in user with the 'usuario' field before saving
            receita = form.save(commit=False)
            receita.usuario = request.user  # Assign the logged-in user to the 'usuario' field
            receita.save()
            messages.success(request, 'Receita cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar Receita. Verifique os campos.')
    else:
        form = ReceitaForm()

    return render(request, 'agendaFinanceiraApp/cadastroReceita.html', {'form': form})

# Visualização para detalhar, atualizar e excluir receitas
#class ReceitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Receita.objects.all()
    #serializer_class = ReceitaSerializer
    

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

@login_required  # Ensure that the user is logged in to access this view
def saldoinicial(request):
    if request.method == 'POST':
        form = SaldoForm(request.POST)
        if form.is_valid():
            # Associate the logged-in user with the 'usuario' field before saving
            saldo = form.save(commit=False)
            saldo.usuario = request.user  # Assign the logged-in user to the 'usuario' field
            saldo.save()
            messages.success(request, 'Saldo Inicial cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar Saldo Inicial. Verifique os campos.')
    else:
        form = SaldoForm()

    return render(request, 'agendaFinanceiraApp/cadastroSaldoinicial.html', {'form': form})


@login_required  # Ensure that the user is logged in to access this view
def saldoatual(request):
    if request.method == 'POST':
        form = SaldoAtlForm(request.POST)
        if form.is_valid():
            # Associate the logged-in user with the 'usuario' field before saving
            atual = form.save(commit=False)
            atual.usuario = request.user  # Assign the logged-in user to the 'usuario' field
            atual.save()
            messages.success(request, 'Saldo Atual cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar Saldo Atual. Verifique os campos.')
    else:
        form = SaldoAtlForm()

    return render(request, 'agendaFinanceiraApp/cadastroSaldoatual.html', {'form': form})

from datetime import datetime

@login_required
def update_saldo_atual(request, pk):
    saldoatual = get_object_or_404(SaldoAtual, pk=pk)
    
    if request.method == 'POST':
        form = SaldoAtlForm(request.POST, instance=saldoatual)
        if form.is_valid():
            # Set the date_modificacao field to the current date and time
            saldoatual.date_modificacao = datetime.now()
            form.save()
            return redirect('saldoatual')
    else:
        form = SaldoAtlForm(instance=saldoatual)
    
    return render(request, 'agendaFinanceiraApp/update_saldo_atual.html', {'form': form, 'saldoatual': saldoatual})

    
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


def receita_list(request):
    usuario = request.user
    cadastros = Receita.objects.filter(usuario=usuario.id)
    return render(request, 'receita_list.html', {
        'cadastros': cadastros
    })
    
def saldoatual_list(request):
    usuario = request.user
    cadastros = SaldoAtual.objects.filter(usuario=usuario.id)
    
    for cadastro in cadastros:
        # Calculate the difference between date_modificacao and created_at
        cadastro.date_diff = cadastro.date_modificacao - cadastro.created_at
        # Calculate days, hours, and minutes
        days, seconds = cadastro.date_diff.days, cadastro.date_diff.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        # Format the duration
        cadastro.formatted_date_diff = f"{days} days, {hours} hours, {minutes} minutes"

    return render(request, 'saldoatual_list.html', {'cadastros': cadastros})
    


class ListarLancamentosView(ListView):
    model = LancamentoContasPagar
    template_name = 'view_apagar.html'
    context_object_name = 'lancamentos'
    
    


