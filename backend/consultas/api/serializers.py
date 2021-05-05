from rest_framework.serializers import ModelSerializer
from consultas.models import Consulta
from agendas.models import Agenda, Horario
from agendas.api.serializers import AgendaSerializer
from medicos.api.serializers import MedicoSerializer
from rest_framework import serializers


class ConsultaSerializer(ModelSerializer):
    medico = MedicoSerializer(read_only=True)
    class Meta:
        model = Consulta
        fields = ['id','dia','horario','data_agendamento','medico']
        read_only_fields = ['id','dia','horario','data_agendamento','medico']