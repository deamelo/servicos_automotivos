from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
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

        return HttpResponse('OI')

def atualiza_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    return JsonResponse(cliente_json)