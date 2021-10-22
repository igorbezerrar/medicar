from rest_framework import serializers

from .models import Especialidade, Medico, Agenda, Consultas, HORARIOS
from django.contrib.auth.models import User

from datetime import datetime


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username",
            "email"
        )


class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields = (
            "id_especialidade",
            "nome"
        )


class MedicoSerializer(serializers.ModelSerializer):

    especialidade = EspecialidadeSerializer()

    class Meta:
        model = Medico
        fields = (
              'id_medico',
              'crm',
              'nome',
              "especialidade",
        )

class AgendaSerializer(serializers.Serializer):

    id_agenda = serializers.IntegerField()
    medico = MedicoSerializer(read_only=True)
    dia = serializers.DateField()
    horarios = serializers.MultipleChoiceField(choices=HORARIOS)

    class Meta:
        model = Agenda
        fields = (
                "id_agenda",
                "medico",
                "dia",
                "horarios"
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if str(instance.dia) == datetime.today().strftime("%Y-%m-%d"):
            horarios = instance.horarios
            horas_disponiveis = []
            for h in horarios:
                if h > datetime.now().strftime("%H:%M"):
                    horas_disponiveis.append(h)
            representation['horarios'] = horas_disponiveis

        return representation


class ConsultaSerializer(serializers.ModelSerializer):
    #Nexted Relationship
    medico = MedicoSerializer(read_only=True)

    class Meta:
        model = Consultas
        fields = (
                "id_consulta",
                "dia",
                "horario",
                "data_agendamento",
                "medico"
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if str(instance.dia) == datetime.today().strftime("%Y-%m-%d"):
            if str(instance.horario) < datetime.now().strftime("%H:%M"):
                representation.clear()

        return representation
