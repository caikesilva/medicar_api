from rest_framework.serializers import ModelSerializer
from especialidades.models import Especialidade

class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'