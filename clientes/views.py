from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect
import re
import json

from .models import Cliente, Carro

def clientes(request):
    if request.method == 'GET':
        listar_clientes = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': listar_clientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        marcas = request.POST.getlist('marca')
        modelos = request.POST.getlist('modelo')
        placas = request.POST.getlist('placa')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            #TODO: Adicionar mensagens
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, "carros": zip(marcas, modelos, placas)})

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            #TODO: Adicionar mensagens
             return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, "carros": zip(marcas, modelos, placas)})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf,
        )

        cliente.save()

        for marca, modelo, placa in zip(marcas, modelos, placas):
            carro = Carro(marca=marca, modelo=modelo, placa=placa, cliente=cliente)
            carro.save()

        return HttpResponse(carro)

def atualiza_cliente(request):
    get_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=get_cliente)
    carros = Carro.objects.filter(cliente=cliente[0])

    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]

    data = {'cliente': cliente_json, 'carros': carros_json, 'cliente_id': cliente_id}


    return JsonResponse(data)

@csrf_exempt
def atualiza_carro(request, id):
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    placa = request.POST.get('placa')

    carro = Carro.objects.get(id=id)
    placa_carro = Carro.objects.filter(placa=placa).exclude(id=id)
    print(placa_carro)
    if placa_carro.exists():
        return HttpResponse('Placa já existe')

    carro.marca = marca
    carro.modelo = modelo
    carro.placa = placa
    carro.save()
    return HttpResponse('Dados alterados com sucesso')

def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=atualiza_cliente&id_cliente={id}')
    except Carro.DoesNotExist:
        return redirect(reverse('clientes')+f'?aba=atualiza_cliente&id_cliente={id}')


