from django.http import JsonResponse
from datetime import date, datetime

from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status


from .models import Consultas, Agenda,Medico, Especialidade
from .serializers import ConsultaSerializer,AgendaSerializer,EspecialidadeSerializer,MedicoSerializer, UsuarioSerializer

from django_filters import rest_framework as filters
from .filterset import EspecialidadeFilter, MedicoFilter, AgendaFilter, ConsultaFilter

from rest_framework.authtoken.models import Token
from rest_framework.response import Response


@authentication_classes([])
@permission_classes([])
class UsuarioViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        username = self.request.data['username']
        password = self.request.data['password']
        email = self.request.data['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        Token.objects.create(user=user)
        serializer = UsuarioSerializer(user)

        return Response(serializer.data)


@authentication_classes([])
@permission_classes([])
class UserLogin(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        username = request.data['username']

        if username is None:
            return Response({'error': 'Usuario ou Email não informado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
            if not user.check_password(request.data['password']):
                return Response({'error': 'Usuario ou senha incorreto'}, status=status.HTTP_400_BAD_REQUEST)

            token = Token.objects.get(user=user)
            serializer = UsuarioSerializer(user)
            return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'Usuario não encontrato'}, status=status.HTTP_404_NOT_FOUND)


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EspecialidadeFilter


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MedicoFilter
    def get_queryset(self):
        especialidade = self.request.query_params.getlist('especialidade')
        if especialidade:
            return self.queryset.filter(especialidade__in=especialidade)
        return self.queryset.all()


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AgendaFilter



class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultaSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ConsultaFilter

    def create(self, request, *args, **kwargs):
        agenda_id = self.request.data['agenda_id']
        hora = self.request.data['horario']
        usuario = request.user

        # recuperando dados da agenda selecionada
        try:
            agenda = Agenda.objects.get(id_agenda=agenda_id)
        except Agenda.DoesNotExist:
            return JsonResponse({'error': 'Agenda inexistente!'}, status=status.HTTP_404_NOT_FOUND)


        # verificando se este usuario ja possui agenda para mesmo dia e horario
        consulta = Consultas.objects.filter(dia=agenda.dia, horario=hora, usuario=usuario)
        if consulta:
            return JsonResponse({'error': 'Você já possui uma consulta para mesmo horário e dia!'}, status=status.HTTP_409_CONFLICT)

        # verificando se este dia e horario está disponivel para agendamento
        consulta = Consultas.objects.filter(dia=agenda.dia, horario=hora, medico=agenda.medico)
        if consulta:
            return JsonResponse({'error': 'Este horario para esse dia já está preenchido!'}, status=status.HTTP_409_CONFLICT)

        horarios = agenda.horarios
        if hora not in horarios:
            return JsonResponse({'error': 'Horário indisponivel nessa agenda!'}, status=status.HTTP_404_NOT_FOUND)

        hora_agenda = int(hora.split(':')[0])
        minuto_agenda = int(hora.split(':')[1])

        hora_sistema = datetime.now().hour
        minuto_sistema = datetime.now().minute

        if agenda.dia == date.today():
            if hora_agenda < hora_sistema or (hora_agenda == hora_sistema and minuto_agenda <= minuto_sistema):
                return JsonResponse({'error': 'Impossível marcar consulta para horario que já passou!'}, status=status.HTTP_409_CONFLICT)

        consulta = Consultas(dia=agenda.dia, horario=hora, medico=agenda.medico, usuario=usuario)
        consulta.save()
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        consulta = self.get_object()
        usuario = request.user

        if consulta.dia < date.today():
            return JsonResponse({'error': 'Essa consulta já ocorreu!'}, status=status.HTTP_409_CONFLICT)

        if consulta.usuario == usuario:
            consulta.delete()
            return Response(None)
        else:
            return JsonResponse({'error': 'Impossivel deletar, não foi marcada por você!'}, status=status.HTTP_409_CONFLICT)
