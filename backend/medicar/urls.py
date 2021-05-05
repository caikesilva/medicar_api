from django.contrib import admin
from django.urls import path, include
from especialidades.api.viewsets import EspecialidadeViewSet
from medicos.api.viewsets import MedicoViewSet
from agendas.api.viewsets import AgendaViewSet
from consultas.api.viewsets import ConsultaViewSet
from rest_framework import routers
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'agendas', AgendaViewSet, basename='Agenda')
router.register(r'consultas', ConsultaViewSet, basename='Consulta')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view()),
    path('accounts/registration/', RegisterView.as_view()),
]
