from django.forms import ModelForm
from .models import Servico, CategoriaManutencao


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

        # self.fields['categoria_manutencao'].choices = (('1', 'teste1'), ('2', 'teste2'), ('3', 'teste3'), ('4', 'teste4'))
        choices = list()
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display()))

        self.fields['categoria_manutencao'].choices = choices

