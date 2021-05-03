from django.db import models
from especialidades.models import Especialidade
# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=250, null=False, blank=False)
    crm = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=250)
    telefone = models.CharField(max_length=15)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    