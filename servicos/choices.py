from django.db.models import TextChoices

class ChoicesCategoriaManutenção(TextChoices):
    TROCAR_OLEO= 'TO', 'Troca de óleo'
    TROCAR_VALVULA_MOTOR = 'TVM', 'Troca de válvula do motor'
    BALANCEAMENTO = 'BLC', 'Balanceamento'
    TROCAR_FILTRO_AR = 'TFA', 'Troca de filtro de ar condocionado'