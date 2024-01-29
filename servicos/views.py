from django.shortcuts import render, get_object_or_404

from .models import Servico
from .forms import ServicoForm
from django.http import HttpResponse


def novo_servico(request):
    if request.method == 'GET':
        form = ServicoForm()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == 'POST':
        form = ServicoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso!')
        else:
            return render(request, 'novo_servico.html', {'form': form})

        # if form.is_valid():
        #     form.save()
        #     return render(request, 'novo_servico.html', {'form': form})
        # else:
        #     return render(request, 'novo_servico.html', {'form': form})

def listar_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})
    
def servico(request, identificador):
    servico = get_object_or_404(Servico,identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})