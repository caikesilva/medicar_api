from rest_framework.viewsets import ModelViewSet
from .serializers import AgendaSerializer
from agendas.models import Agenda
from datetime import date
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AgendaViewSet(ModelViewSet):
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get']    

    def get_queryset(self):
        
        queryset = Agenda.objects.filter(dia__gte=date.today()).order_by('dia')
        data_inicio = self.request.query_params.get('data_inicio', None)
        data_final = self.request.query_params.get('data_final', None)
        medico = self.request.query_params.get('medico', None)
        especialidade = self.request.query_params.get('especialidade', None)
    
        if medico:
            queryset = queryset.filter(medico=medico)
        
        if especialidade:
            queryset = queryset.filter(medico__especialidade=especialidade)

        if data_inicio and data_final:
            queryset = queryset.filter(dia__range=(data_inicio,data_final))        

        return queryset
