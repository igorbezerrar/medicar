from django.utils import timezone

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from rest_framework import generics
from .models import Consultas, Agenda,Medico, Especialidade
from .serializers import ConsultaSerializer,AgendaSerializer,EspecialidadeSerializer,MedicoSerializer

"""
API versao 1
"""

class EspecialidadesAPIView(generics.ListCreateAPIView):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search is not None:
            return self.queryset.filter(nome__contains=search)
        return self.queryset.all()


class MedicoAPIView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        especialidade = self.request.query_params.getlist('especialidade')
        if search is not None:
            return self.queryset.filter(nome__contains=search).filter(especialidade__in=especialidade)
        return self.queryset.all()


class AgendaAPIView(generics.ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class ConsultaAPIView(generics.ListCreateAPIView):
    queryset = Consultas.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        return self.queryset.filter(dia__gte=timezone.now()).order_by('dia')


"""
API versao 2
"""

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search is not None:
            return self.queryset.filter(nome__contains=search)
        return self.queryset.all()


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        especialidade = self.request.query_params.getlist('especialidade')
        if search is not None:
            return self.queryset.filter(nome__contains=search).filter(especialidade__in=especialidade)
        return self.queryset.all()


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    @action(detail=True, methods=['get'])
    def medico(self, request, pk=None):
        agenda = self.get_object()
        query_set = Medico.objects.filter(nome=agenda.medico)
        serializer = MedicoSerializer(query_set, many=True)
        return Response(serializer.data)


class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        return self.queryset.filter(dia__gte=timezone.now()).order_by('dia')