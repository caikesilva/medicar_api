from rest_framework.serializers import ModelSerializer
from especialidades.api.serializers import EspecialidadeSerializer
from medicos.models import Medico

class MedicoSerializer(ModelSerializer):
    especialidade = EspecialidadeSerializer()
    
    class Meta:
        model = Medico
        fields = ['id','crm','nome','especialidade']