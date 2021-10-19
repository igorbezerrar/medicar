from .models import Especialidade, Medico, Agenda, Consultas
from django_filters import rest_framework as filters
from django_filters import BaseInFilter, NumberFilter

class EspecialidadeFilter(filters.FilterSet):
    search = filters.CharFilter(field_name="nome", lookup_expr='contains')

    class Meta:
        model = Especialidade
        fields = ['nome']


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class MedicoFilter(filters.FilterSet):
    search = filters.CharFilter(field_name="nome", lookup_expr='contains')
    especialidade__in = NumberInFilter(field_name="especialidade", lookup_expr="in")

    class Meta:
        model = Medico
        fields = ['search']


class AgendaFilter(filters.FilterSet):

    medico = filters.CharFilter(field_name="medico")
    especialidade = filters.NumberFilter(field_name="medico__especialidade")
    data_inicio = filters.DateFilter(field_name="dia", lookup_expr="gte")
    data_final = filters.DateFilter(field_name="dia", lookup_expr="lte")

    class Meta:
        model = Agenda
        fields = ['medico', 'especialidade', 'data_inicio', 'data_final']


class ConsultaFilter(filters.FilterSet):
    search = filters.CharFilter(field_name="nome", lookup_expr='contains')
    especialidade__in = NumberInFilter(field_name="especialidade", lookup_expr="in")

    class Meta:
        model = Medico
        fields = ['search']
