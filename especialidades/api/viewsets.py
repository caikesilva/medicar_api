from rest_framework.viewsets import ModelViewSet
from especialidades.models import Especialidade
from .serializers import EspecialidadeSerializer
from rest_framework.filters import SearchFilter #Filtro
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get']
    filter_backends = [SearchFilter]
    search_fields = ['^nome']
