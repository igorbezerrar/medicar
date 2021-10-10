from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Especialidade, Medico, Agenda, Consultas
from .serializers import EspecialidadeSerializer, MedicoSerializer, AgendaSerializer, ConsultaSerializer


class EspecialidadeAPIView(APIView):
    """
    API que busca as especialidades médicas
    """
    def get(self, request):
        especialidades = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(especialidades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EspecialidadeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConsultaAPIView(APIView):
    """
    API que lista todas as consultas marcadas
    """
    def get(self, request):
        consultas = Consultas.objects.all()
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data)

class MedicoAPIView(APIView):
    """
    API que busca as médicos salvos
    """
    def get(self, request):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)

class AgendaAPIView(APIView):
    """
    API que busca as consultas salvas
    """
    def get(self, request):
        consultas = Agenda.objects.all()
        serializer = AgendaSerializer(consultas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AgendaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

