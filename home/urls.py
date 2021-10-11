from rest_framework.routers import SimpleRouter

from .views import (
    EspecialidadeViewSet,MedicoViewSet, AgendaViewSet, ConsultasViewSet
)

router = SimpleRouter()
router.register('especialidades', EspecialidadeViewSet)
router.register('medicos', MedicoViewSet)
router.register('agenda', AgendaViewSet)
router.register('consultas', ConsultasViewSet)

