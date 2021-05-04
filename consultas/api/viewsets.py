from rest_framework.viewsets import ModelViewSet
from .serializers import ConsultaSerializer
from consultas.models import Consulta
from agendas.models import Agenda
from horarios.models import Horario
from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from datetime import date

class ConsultaViewSet(ModelViewSet):
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = Consulta.objects.filter(usuario=self.request.user).exclude(dia__lte=date.today())
        return queryset

    def create(self, request, *args, **kwargs):
        try:
    
            ag = Agenda.objects.get(id=request.data['agenda_id'],horarios__horario=request.data['horario'])
            if ag:
        
                if Consulta.objects.filter(dia=ag.dia,medico=ag.medico,horario=request.data['horario'],usuario=request.user):
                    return Response({"detail": "Voçê já possui uma consulta agendada"})
                
                elif ag.dia < date.today():
                    return Response({"detail": "Não é possivel marcar uma consulta para dias anteriores!"})

                elif Consulta.objects.filter(dia=ag.dia,medico=ag.medico,horario=request.data['horario']):
                    return Response({"detail": "Já existe uma consulta agendada para este dia e horario!"})
            
            c = Consulta.objects.create(dia=ag.dia,medico=ag.medico,horario=request.data['horario'],usuario=request.user) 
            serializer = ConsultaSerializer(c)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        except ObjectDoesNotExist:
            raise ValidationError({"detail":"Agenda não existe"})


    def destroy(self, request, *args, **kwargs):
        
        try:
            if Consulta.objects.get(id=kwargs['pk']):
                consulta = Consulta.objects.filter(id=kwargs['pk'],usuario=request.user)
                for c in consulta:
                    if c.dia < date.today():
                        return Response({"detail": "Não é possivel deletar uma consulta que já passou!"}) 
                    c.delete()
                    return Response([]) 
                return Response({"detail": "Voçê não tem permissão para deletar esta consulta!"})       
        except ObjectDoesNotExist:
            raise ValidationError({"detail":"Consulta não existe"})