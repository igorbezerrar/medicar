from rest_framework import serializers, fields
from .models import Especialidade, Medico, Agenda, Consultas, MY_CHOICES


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

    medico = EspecialidadeSerializer(read_only=True)
    horas = fields.MultipleChoiceField(choices=MY_CHOICES)
    class Meta:
        model = Agenda
        fields = (
                "id_agenda",
                "medico",
                "dia",
                "horas",
        )

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = (
                "id_consulta",
                "dia",
                "horario",
                "data_agendamento",
                "medico"
        )