from django.forms import ModelForm
from django.urls import reverse
from django import forms
from .models import Cliente, Receita, Despesa, LancamentoContasPagar, Fornecedor
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper



from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)

class FornecedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FornecedorForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-fornecedor-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div(Field('nm_fornecedor'), css_class="col-md-6"),
                Div(Field('telefone'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('endereco'), css_class="col-md-6"),
                Div(Field('cidade'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('uf'), css_class="col-md-2"),
                Div(Field('tipo'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('email'), css_class="col-md-4"),
                css_class="row"),
            Div(
                Div(Field('cnpj_cpf'), css_class="col-md-3"),
                css_class="row"),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )
    class Meta:
        model = Fornecedor
        fields = ['nm_fornecedor','endereco','cidade','uf','telefone','email','tipo','cnpj_cpf']
        exclude=['cd_forncedor', 'usuario']
            
                



class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-cliente-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div('nm_cliente', css_class="col-md-6"),
                Div('telefone', css_class="col-md-3"),
                css_class="row"),
            Div(
                Div('endereco', css_class="col-md-6"),
                Div('cidade', css_class="col-md-3"),
                css_class="row"),
            Div(
                Div('uf', css_class="col-md-2"),
                Div('tipo', css_class="col-md-3"),
                css_class="row"),
            Div(
                Div('email', css_class="col-md-4"),
                css_class="row"),
            Div(
                Div('cnpj_cpf', css_class="col-md-3"),
                css_class="row"),
            Submit('submit', 'Enviar', css_class='btn btn-success col-centered')
        )

    class Meta:
        model = Cliente
        fields = ['nm_cliente', 'endereco', 'cidade', 'uf', 'telefone', 'email', 'tipo', 'cnpj_cpf']
        exclude = ['cd_cliente', 'usuario']
        

class DespesaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DespesaForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-despesa-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_credor'), css_class="col-md-6"),
                Div(Field('valor'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('data_vencimento'), css_class="col-md-6"),
                Div(Field('situacao'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('tipo_despesa'), css_class="col-md-2"),
                Div(Field('modo_pag'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('image'), css_class="col-md-4"),
                css_class="row"),
            Div(
                Div(Field('observacoes'), css_class="col-md-3"),
                css_class="row"),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )
    class Meta:
        model = Despesa
        fields = ['nome_credor','valor','data_vencimento','situacao','observacoes','tipo_despesa','modo_pag','image']
        exclude=['id_despesa', 'usuario','created_at']
        

class ReceitaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceitaForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-receita-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_pagador'), css_class="col-md-6"),
                Div(Field('valor'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('data_entrada'), css_class="col-md-6"),
                Div(Field('tipo_recebimento'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('forma_recebimento'), css_class="col-md-2"),
                Div(Field('situacao'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('observacoes'), css_class="col-md-3"),
                css_class="row"),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )
    class Meta:
        model = Receita
        fields = ['valor','data_entrada','nome_pagador','forma_recebimento','situacao','observacoes','tipo_recebimento']
        exclude=[ 'usuario','created_at']        
        

class LancamentoContasPagarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LancamentoContasPagarForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-contasapagar-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div(Field('data_docto'), css_class="col-md-3"),
                Div(Field('despesa'), css_class="col-md-4"),
                css_class="row"),
            Div(
                Div(Field('documento'), css_class="col-md-3"),
                Div(Field('plano_conta'), css_class="col-md-3"),
                Div(Field('conta'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('pago_pelo_banco'), css_class="col-md-4"),
                Div(Field('valor'), css_class="col-md-2"),
                Div(Field('parcelas'), css_class="col-md-2"),
                css_class="row"),
            Div(
                Div(Field('valor_parcela'), css_class="col-md-3"),
                Div(Field('vencimento'), css_class="col-md-3"),
                css_class="row"),
            Div(
                Div(Field('pagamento'), css_class="col-md-4"),
                Div(Field('status'), css_class="col-md-4"),
                css_class="row"),
            Div(
                Div(Field('tipo'), css_class="col-md-4"),
                Div(Field('fornecedor'), css_class="col-md-8"),
                css_class="row"),
            Div(
                Div(Field('descricao'), css_class="col-md-8"),
                css_class="row"),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )

    class Meta:
        model = LancamentoContasPagar
        fields = ['data_docto', 'documento', 'plano_conta', 'conta', 'documento', 'tipo', 'fornecedor',
                  'descricao', 'pago_pelo_banco', 'valor', 'parcelas', 'valor_parcela', 'vencimento', 'pagamento',
                  'status', 'despesa']
        widgets = {
            'fornecedor': Select2MultipleWidget,
        }
      