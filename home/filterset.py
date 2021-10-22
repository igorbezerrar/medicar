from .models import Agenda, Consultas
from django_filters import rest_framework as filters
from django.utils import timezone


class AgendaFilter(filters.FilterSet):

    medico = filters.NumberFilter(field_name="medico")
    especialidade = filters.NumberFilter(field_name="medico__especialidade")
    data_inicio = filters.DateFilter(field_name="dia", lookup_expr="gte")
    data_final = filters.DateFilter(field_name="dia", lookup_expr="lte")

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(dia__gte=timezone.now()).order_by('dia')

    class Meta:
        model = Agenda
        fields = ['medico', 'especialidade', 'data_inicio', 'data_final']


class ConsultaFilter(filters.FilterSet):

    @property
    def qs(self):
        parent = super().qs
        return parent.filter(dia__gte=timezone.now()).order_by('dia', 'horario')

    class Meta:
        model = Consultas
        fields = ['dia']
