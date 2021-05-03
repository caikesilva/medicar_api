from django.db import models
from medicos.models import Medico
from horarios.models import Horario 
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False, blank=False)
    dia = models.DateField(null=False, blank=False)
    horarios = models.ManyToManyField(Horario)

    def clean(self):
        if self.dia < date.today():
            raise ValidationError("Não é possível criar uma agenda para um médico em um dia passado!")  

        if Agenda.objects.filter(medico=self.medico, dia=self.dia).exists():
            raise ValidationError("Não é possível criar mais de uma agenda para um médico em um mesmo dia!")

    def __str__(self):
        return self.medico.nome
    