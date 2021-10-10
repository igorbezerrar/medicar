from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    EspecialidadesAPIView, MedicoAPIView, AgendaAPIView, ConsultaAPIView,
    EspecialidadeViewSet,MedicoViewSet, AgendaViewSet, ConsultasViewSet
)

router = SimpleRouter()
router.register('especialidades', EspecialidadeViewSet)
router.register('medicos', MedicoViewSet)
router.register('agenda', AgendaViewSet)
router.register('consultas', ConsultasViewSet)

urlpatterns = [
    path('especialidades/', EspecialidadesAPIView.as_view(), name="especialidade"),
    path('medicos/', MedicoAPIView.as_view(), name="medicos"),
    path('agendas/', AgendaAPIView.as_view(), name="agendas"),
    path('consultas/', ConsultaAPIView.as_view(), name="consultas"),
]
