from rest_framework import serializers, fields

from .models import Especialidade, Medico, Agenda, Consultas, HORARIOS
from django.contrib.auth.models import User


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


class AgendaSerializer(serializers.ModelSerializer):

    medico = MedicoSerializer(read_only=True)
    horarios = fields.MultipleChoiceField(choices=HORARIOS)

    class Meta:
        model = Agenda
        fields = (
                "id_agenda",
                "medico",
                "dia",
                "horarios"
        )

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
