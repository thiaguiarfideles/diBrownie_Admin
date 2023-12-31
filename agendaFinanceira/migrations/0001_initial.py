# Generated by Django 3.2.9 on 2023-10-10 18:48

import agendaFinanceira.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cd_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('nm_cliente', models.CharField(max_length=255, verbose_name='Nome do Cliente')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('tipo', models.CharField(choices=[('Pessoa Jurídica', 'Pessoa Jurídica'), ('Pessoa Física', 'Pessoa Física')], max_length=15, verbose_name='Tipo')),
                ('cnpj_cpf', models.CharField(max_length=18, unique=True, verbose_name='CNPJ/CPF')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id_despesa', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_vencimento', models.DateTimeField()),
                ('situacao', models.CharField(choices=[('Em Aberto', 'Em Aberto'), ('Pago', 'Pago')], max_length=11)),
                ('observacoes', models.TextField()),
                ('tipo_despesa', models.CharField(choices=[('CONTAS', 'Contas'), ('COMPRAS_MERCADO', 'Compras Mercado'), ('COMPRAS_HORTIFRUTI', 'Compras Hortifruti'), ('COMPRAS_RESTAURANTE', 'Compras Restaurante'), ('COMPRAS_GERAL', 'Compras geral'), ('COMBUSTIVEL', 'Combustível'), ('ALUGUEL', 'Aluguel'), ('TV_INTERNET', 'TV/Internet'), ('TELEFONE', 'Telefone'), ('CARRO', 'Carro'), ('SEGURO', 'Seguro'), ('AGUA', 'Água'), ('LUZ', 'Luz'), ('CARTAO_CREDITO', 'Cartão de Crédito'), ('OUTROS', 'Outros')], default='CONTAS', max_length=90, verbose_name='Tipo de Despesa')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Enviado em')),
                ('modo_pag', models.CharField(choices=[('CARTAO_CREDITO', 'Cartão de Crédito'), ('DINHEIRO', 'Dinheiro'), ('PIX', 'Pix')], default='Cartão de Crédito', max_length=30, verbose_name='Método de Pagamento')),
                ('image', models.ImageField(blank=True, null=True, upload_to=agendaFinanceira.models.upload_to_despesa)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('cd_forncedor', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('nm_fornecedor', models.CharField(max_length=255, verbose_name='Nome do Fornecedor')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('tipo', models.CharField(choices=[('Pessoa Jurídica', 'Pessoa Jurídica'), ('Pessoa Física', 'Pessoa Física')], max_length=15, verbose_name='Tipo')),
                ('cnpj_cpf', models.CharField(max_length=18, unique=True, verbose_name='CNPJ/CPF')),
            ],
            options={
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_gasto', models.DateTimeField()),
                ('tipo_gasto', models.CharField(choices=[('CUSTOS_VARIAVEIS', 'Custos Variáveis'), ('CUSTOS_VARIAVEIS_MERCADORIA', 'Mercadoria para Revenda'), ('CUSTOS_VARIAVEIS_MATERIA_PRIMA', 'Matéria-prima'), ('CUSTOS_VARIAVEIS_INSUMOS', 'Insumos'), ('DESPESAS_OCUPACAO', 'Despesas com Ocupação'), ('DESPESAS_OCUPACAO_AGUA', 'Água'), ('DESPESAS_OCUPACAO_ALUGUEL', 'Aluguel'), ('DESPESAS_OCUPACAO_CONDOMINIO', 'Condomínio'), ('DESPESAS_OCUPACAO_TELEFONE_INTERNET', 'Telefone + Internet'), ('DESPESAS_OCUPACAO_IPTU', 'IPTU'), ('DESPESAS_OCUPACAO_LIMPEZA_CONSERVACAO', 'Limpeza e Conservação'), ('DESPESAS_OCUPACAO_ENERGIA_ELETRICA', 'Energia Elétrica'), ('DESPESAS_SERVICOS', 'Despesas com Serviços'), ('DESPESAS_SERVICOS_CONTABILIDADE', 'Contabilidade'), ('DESPESAS_SERVICOS_PUBLICIDADE_PROPAGANDA', 'Publicidade e Propaganda'), ('DESPESAS_SERVICOS_SERVICOS_JURIDICOS', 'Serviços Jurídicos'), ('DESPESAS_SERVICOS_WEBDESIGNER', 'Webdesigner'), ('DESPESAS_SERVICOS_DESIGNER', 'Designer'), ('DESPESAS_SERVICOS_SERVICOS_TI', 'Serviços de TI'), ('DESPESAS_PESSOAL', 'Despesas com Pessoal'), ('DESPESAS_PESSOAL_PRO_LABORE', 'Pró-Labore'), ('DESPESAS_PESSOAL_FOLHA_PAGAMENTO', 'Folha de Pagamento'), ('DESPESAS_PESSOAL_VALE_TRANSPORTE', 'Vale Transporte'), ('DESPESAS_PESSOAL_VALE_REFEICAO', 'Vale Refeição'), ('DESPESAS_PESSOAL_ASSISTENCIA_MEDICA', 'Assistência Médica'), ('DESPESAS_PESSOAL_ASSISTENCIA_ODONTO', 'Assistência Odonto'), ('DESPESAS_PESSOAL_INSS', 'INSS'), ('DESPESAS_PESSOAL_FGTS', 'FGTS'), ('DEDUCOES_VENDAS', 'Deduções sobre Vendas'), ('DEDUCOES_VENDAS_DAS_SIMPLES_NACIONAL', 'DAS - Simples Nacional'), ('DEDUCOES_VENDAS_PIS', 'PIS'), ('DEDUCOES_VENDAS_COFINS', 'COFINS'), ('DEDUCOES_VENDAS_ISS', 'ISS'), ('DEDUCOES_VENDAS_IPI', 'IPI'), ('DEDUCOES_VENDAS_ICMS', 'ICMS'), ('DEDUCOES_VENDAS_COMISSOES', 'Comissões'), ('IMPOSTOS_DIRETOS', 'Impostos Diretos'), ('IMPOSTOS_DIRETOS_IRPJ', 'IRPJ'), ('IMPOSTOS_DIRETOS_CSLL', 'CSLL')], default='CUSTOS_VARIAVEIS', max_length=100, verbose_name='Tipo de Gasto')),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LancamentoContasPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=255, verbose_name='Numero Documento')),
                ('data_docto', models.DateField(verbose_name='Data Dcto')),
                ('plano_conta', models.CharField(max_length=255, verbose_name='Plano de Conta')),
                ('conta', models.CharField(max_length=255, verbose_name='Conta')),
                ('tipo', models.CharField(choices=[('Receita', 'Receita'), ('Outros', 'Outros')], max_length=15, verbose_name='Tipo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('pago_pelo_banco', models.BooleanField(choices=[('SANTANDER', 'SANTANDER'), ('BRADESCO', 'BRADESCO'), ('ITAU', 'ITAU'), ('CAIXA', 'CAIXA'), ('BANCO DO BRASIL', 'BANCO DO BRASIL'), ('PICPAY', 'PICPAY'), ('MERCADO PAGO', 'MERCADO PAGO'), ('SAFRA PAY', 'SAFRA PAY')], default='SANTANDER', verbose_name='Pago pelo Banco')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor R$')),
                ('parcelas', models.IntegerField(verbose_name='Parcelas')),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Parcela')),
                ('vencimento', models.DateField(verbose_name='Vencimento')),
                ('pagamento', models.DateField(blank=True, null=True, verbose_name='Pagamento')),
                ('status', models.CharField(choices=[('Em Aberto', 'Em Aberto'), ('Pago', 'Pago')], max_length=15, verbose_name='Status')),
                ('status_pagamento', models.CharField(choices=[('Não Pago', 'Não Pago'), ('Pago', 'Pago')], default=django.utils.timezone.now, max_length=30, verbose_name='Status do Pagamento')),
            ],
            options={
                'verbose_name_plural': 'Lançamentos Contas a Pagar',
            },
        ),
        migrations.CreateModel(
            name='LancamentoContasReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_documento', models.CharField(max_length=255, verbose_name='Numero Documento')),
                ('data_dcto', models.DateField(verbose_name='Data Dcto')),
                ('plano_conta', models.CharField(max_length=255, verbose_name='Plano de Conta')),
                ('conta', models.CharField(max_length=255, verbose_name='Conta')),
                ('tipo', models.CharField(choices=[('Receita', 'Receita'), ('Outros', 'Outros')], max_length=15, verbose_name='Tipo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('recebido_banco', models.BooleanField(default=False, verbose_name='Recebido pelo banco')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor R$')),
                ('parcelas', models.IntegerField(verbose_name='Parcelas')),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Parcela')),
                ('vencimento', models.DateField(verbose_name='Vencimento')),
                ('recebimento', models.DateField(blank=True, null=True, verbose_name='Recebimento')),
                ('status', models.CharField(choices=[('Em Aberto', 'Em Aberto'), ('Pago', 'Pago')], max_length=15, verbose_name='Status')),
                ('status_recebimento', models.CharField(choices=[('Não Recebido', 'Não Recebido'), ('Recebido', 'Recebido')], max_length=15, verbose_name='Status Recebimento')),
            ],
            options={
                'verbose_name_plural': 'Lançamentos Contas a Receber',
            },
        ),
        migrations.CreateModel(
            name='OrcamentoGastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(choices=[(2023, '2023'), (2024, '2024'), (2025, '2025')], verbose_name='Ano')),
                ('mes', models.CharField(max_length=3, verbose_name='Mês')),
                ('custos_variaveis', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Custos Variáveis')),
                ('despesas_com_ocupacao', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Despesas com Ocupação')),
                ('despesas_com_servicos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Despesas com Serviços')),
                ('despesas_com_pessoal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Despesas com Pessoal')),
                ('deducoes_sobre_vendas', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Deduções sobre Vendas')),
                ('impostos_diretos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Impostos Diretos')),
                ('outras_despesas', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Outras Despesas')),
                ('outras_despesas_2', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Outras Despesas 2')),
                ('outras_despesas_3', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Outras Despesas 3')),
                ('despesas_financeiras', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Despesas Financeiras')),
                ('investimentos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Investimentos')),
                ('gastos_totais', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Gastos Totais')),
            ],
            options={
                'verbose_name_plural': 'Orçamento de Gastos',
            },
        ),
        migrations.CreateModel(
            name='OrcamentoReceitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(choices=[(2023, '2023'), (2024, '2024'), (2025, '2025')], verbose_name='Ano')),
                ('mes', models.CharField(max_length=3, verbose_name='Mês')),
                ('receita_com_produtos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Receita com Produtos')),
                ('receita_com_servicos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Receita com Serviços')),
                ('outras_receitas', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Outras Receitas')),
                ('outras_receitas_2', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Outras Receitas 2')),
                ('outras_receitas_3', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Outras Receitas 3')),
                ('receitas_financeiras', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Receitas Financeiras')),
                ('receitas_totais', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Receitas Totais')),
            ],
            options={
                'verbose_name_plural': 'Orçamento de Receitas',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_entrada', models.DateTimeField()),
                ('nome_pagador', models.CharField(max_length=90)),
                ('forma_recebimento', models.CharField(max_length=90)),
                ('situacao', models.CharField(choices=[('AB', 'Aberto'), ('PG', 'Pago')], max_length=2)),
                ('observacoes', models.TextField()),
                ('tipo_recebimento', models.CharField(choices=[('RECEITA_PRODUTOS', 'Receita com Produtos'), ('RECEITA_SERVICOS', 'Receita com Serviços'), ('OUTRAS_RECEITAS', 'Outras Receitas')], default='OUTRAS_RECEITAS', max_length=90, verbose_name='Tipo de Recebimento')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Enviado em')),
            ],
        ),
        migrations.CreateModel(
            name='SaldoInicial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=100, verbose_name='Nome do Banco')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Saldo Inicial')),
                ('data_inicial', models.DateField(verbose_name='Data Inicial do Saldo')),
            ],
        ),
    ]
