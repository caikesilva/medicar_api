from rest_framework.serializers import ModelSerializer, StringRelatedField
from medicos.api.serializers import MedicoSerializer
from agendas.models import Agenda

class AgendaSerializer(ModelSerializer):
    horarios = StringRelatedField(many=True)
    medico = MedicoSerializer(many=False)
    class Meta:
        model = Agenda
        fields = ['id','medico','dia','horarios']