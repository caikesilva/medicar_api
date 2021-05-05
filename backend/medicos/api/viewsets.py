from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter #Filtro
from django_filters.rest_framework import DjangoFilterBackend #Filtro
from medicos.models import Medico
from .serializers import MedicoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get']
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['especialidade'] 
    search_fields = ['^nome']
