# Generated by Django 3.2.9 on 2023-10-10 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Titulo')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True, verbose_name='Conclusão da Atividade')),
                ('priority', models.BooleanField(default=False, verbose_name='Prioridade')),
                ('date_conclusao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da Atividade')),
            ],
        ),
    ]
