from django.db import models
from agendas.models import Agenda
from medicos.models import Medico
from django.conf import settings

# Create your models here.

class Consulta(models.Model):
    data_agendamento = models.DateTimeField(auto_now_add=True)
    dia = models.DateField()
    horario = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ['dia','horario']

    def __str__(self):
        return str(self.dia)
    