from rest_framework.routers import SimpleRouter

from .views import (
    EspecialidadeViewSet, MedicoViewSet, AgendaViewSet, ConsultasViewSet, UsuarioViewSet, UserLogin
)

router = SimpleRouter()
router.register('rest_auth/registration', UsuarioViewSet)
router.register('login', UserLogin)

router.register('especialidades', EspecialidadeViewSet)
router.register('medicos', MedicoViewSet)
router.register('agenda', AgendaViewSet)
router.register('consultas', ConsultasViewSet)

