import logging
import time
from datetime import datetime

from .models import Pessoas,Cargos
import string
from django.utils.crypto import get_random_string
from django.shortcuts import render
import random
from django.db.models import Count

NUMBER_ENTRIES = 100

def fill_table_cargos():
    cargos_dict = {}
    if not (Cargos.objects.all()):
        Cargos.objects.create(id=1, nome_cargo = "Gerente de Projetos")
        Cargos.objects.create(id=2, nome_cargo="Tecnologia da Informação")
        Cargos.objects.create(id=3, nome_cargo="Serviços Gerais")
        Cargos.objects.create(id=4, nome_cargo="Departamento Pessoal")

def get_random_cargo():
    cargos = Cargos.objects.all()
    random_cargo = random.choice(cargos)
    return random_cargo

def get_random_date():
    date_aux = random.randint(1, int(time.time()))
    return datetime.fromtimestamp(date_aux).strftime('%Y-%m-%d')

def fill_table_pessoas():
    if not (Cargos.objects.all()):
        fill_table_cargos()
    for i in range(0,NUMBER_ENTRIES):
        random_cargo = get_random_cargo()
        generated_string = get_random_string(50, string.ascii_uppercase + string.digits)
        random_admissao = get_random_date()
        Pessoas.objects.create(id=i, cargo = random_cargo, nome = generated_string, admissao=random_admissao)


def questao1(request):
    pessoas = Pessoas.objects.all()
    if not pessoas:
        fill_table_pessoas()
    query_sql = Pessoas.objects.all().order_by('admissao').values_list('nome', 'cargo__nome_cargo').query
    result = Pessoas.objects.all().order_by('admissao').values_list('nome', 'cargo__nome_cargo')

    context = {
        'query_sql' : query_sql,
        'result':result,
    }
    return render(request, "questao1/questao1.html", context=context)

def questao1A(request):
    pessoas = Pessoas.objects.all()
    if not pessoas:
        fill_table_pessoas()
    query_sql = Pessoas.objects.all().order_by('admissao').values_list('nome', 'cargo__nome_cargo').query
    result = Pessoas.objects.all().order_by('admissao').values_list('nome', 'cargo__nome_cargo')
    result_not_formated = Pessoas.objects.all().order_by('admissao')
    context = {
        'query_sql': query_sql,
        'result': result,
        'result_not_formated': result_not_formated
    }
    return render(request, "questao1/questao1.html", context=context)

def questao1B(request):
    pessoas = Pessoas.objects.all()
    if not pessoas:
        fill_table_pessoas()
    query_sql = str(Pessoas.objects.order_by('admissao').values_list('nome', 'cargo__nome_cargo').query) +"  LIMIT 1 "
    result =  Pessoas.objects.order_by('admissao').values_list('nome', 'cargo__nome_cargo').first()
    result_not_formated = Pessoas.objects.all().order_by('admissao').first()
    context = {
        'query_sql': query_sql,
        'result': result,
        'result_not_formated': result_not_formated
    }
    return render(request, "questao1/questao1.html", context=context)

def questao1C(request):
    pessoas = Pessoas.objects.all()
    if not pessoas:
        fill_table_pessoas()
    query_sql = Pessoas.objects.values('cargo__nome_cargo').annotate(frequency=Count('cargo')).query


    result = Pessoas.objects.values('cargo__nome_cargo').annotate(frequency=Count('cargo'))

    result_not_formated = None
    context = {
        'query_sql' : query_sql,
        'result':result,
        'result_not_formated':result_not_formated
    }
    return render(request, "questao1/questao1.html", context=context)

