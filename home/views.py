from django.http import JsonResponse
from django.utils import timezone
from datetime import date, time, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Consultas, Agenda,Medico, Especialidade
from .serializers import ConsultaSerializer,AgendaSerializer,EspecialidadeSerializer,MedicoSerializer

from django_filters import rest_framework as filters
from .filterset import EspecialidadeFilter, MedicoFilter, AgendaFilter

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

    def get_queryset(self):

        medico = self.request.query_params.getlist('medico')
        especialidade = self.request.query_params.getlist('especialidade')
        data_inicio = self.request.query_params.get('data_inicio')
        data_final = self.request.query_params.get('data_final')

        # if medico != [] and especialidade != [] and data_inicio and data_final is not None:
        #     return self.queryset.filter(medico__in=medico,
        #                                 medico__especialidade__in=especialidade,
        #                                 dia__gte=data_inicio,
        #                                 dia__lte=data_final).order_by('dia')
        #
        # if medico != [] and especialidade != []:
        #     return self.queryset.filter(medico__in=medico,
        #                                 medico__especialidade__in=especialidade,
        #                                 dia__gte=timezone.now()).order_by('dia')
        #
        # if medico:
        #     return self.queryset.filter(medico__in=medico,
        #                                 dia__gte=timezone.now()).order_by('dia')
        #
        # if especialidade:
        #     return self.queryset.filter(medico__especialidade__in=especialidade,
        #                                 dia__gte=timezone.now()).order_by('dia')
        #
        # if data_inicio and data_final is not None:
        #     return self.queryset.filter(dia__gte=data_inicio,
        #                                 dia__lte=data_final).order_by('dia')


        return self.queryset.all().order_by('dia')

    # @action(detail=True, methods=['get'])
    # def medico(self, request, pk=None):
    #     agenda = self.get_object()
    #     query_set = Medico.objects.filter(nome=agenda.medico)
    #     serializer = MedicoSerializer(query_set, many=True)
    #     return Response(serializer.data)


class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        print(self.request.user)
        return self.queryset.filter(dia__gte=timezone.now(), usuario=self.request.user).order_by('dia', 'horario')

    def create(self, request, *args, **kwargs):
        agenda_id = self.request.data['agenda_id']
        hora = self.request.data['horario']
        usuario = request.user

        #recuperando dados da agenda selecionada
        agenda = Agenda.objects.get(id_agenda=agenda_id)

        # verificando se este usuario ja possui agenda para mesmo dia e horario
        consulta = Consultas.objects.filter(dia=agenda.dia, horario=hora, usuario=usuario)
        if consulta:
            return JsonResponse({'error': 'Você já possui uma consulta para mesmo horário e dia!'})

        # verificando se este dia e horario está disponivel para agendamento
        consulta = Consultas.objects.filter(dia=agenda.dia, horario=hora, medico=agenda.medico)
        if consulta:
            return JsonResponse({'error': 'Este horario para esse dia já está preenchido!'})

        horarios = agenda.horarios
        if hora not in horarios:
            return JsonResponse({'error': 'Horário indisponivel nessa agenda!'})

        hora_agenda = int(hora.split(':')[0])
        minuto_agenda = int(hora.split(':')[1])
        agora = datetime.now()
        hora_sistema = agora.hour
        minuto_sistema = agora.minute
        print("Agenda: ", hora_agenda, minuto_agenda, "Sistema: ", hora_sistema, minuto_sistema)
        print("Dia agenda: ", agenda.dia, "Dia sistema: ", date.today())
        if agenda.dia == date.today():
            if hora_agenda < hora_sistema or (hora_agenda == hora_sistema and minuto_agenda <= minuto_sistema):
                return JsonResponse({'error': 'Impossível marcar consulta para hora passada!'})

        consulta = Consultas(dia=agenda.dia, horario=hora, medico=agenda.medico, usuario=usuario)
        consulta.save()
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        consulta = self.get_object()
        usuario = request.user

        if consulta.usuario == usuario:
            consulta.delete()
            return Response(None)
        else:
            return JsonResponse({'error': 'Impossivel deletar, não foi marcada por você!'})
