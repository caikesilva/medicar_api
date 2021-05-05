from django.db import models

# Create your models here.

class Horario(models.Model):
    horario = models.TimeField(null=False, blank=False)
    
    def __str__(self):
        return str(self.horario)