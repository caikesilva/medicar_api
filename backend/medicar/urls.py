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




#Personalizando admin

from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group
from allauth.account.models import EmailAddress
from rest_framework.authtoken.models import TokenProxy

admin.site.site_header = 'Medicar'
admin.site.index_title = 'Medicar API'
admin.site.site_title = 'Medicar'

admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
admin.site.unregister(EmailAddress)

