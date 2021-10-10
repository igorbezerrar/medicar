from datetime import datetime

from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.core.exceptions import ValidationError

class Especialidade(models.Model):
    id_especialidade = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nome

class Medico(models.Model):
    id_medico = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(null=False, blank=False, max_length=100)
    crm = models.IntegerField(null=False, blank=False, unique=True)
    email = models.CharField(null=True, blank=True, max_length=100)
    telefone = models.CharField(null=True, blank=True, max_length=11)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def __str__(self):
        return "{}".format(self.nome)

MY_CHOICES = (('14:00', '14:00'),
              ('15:00', '15:00'),
              ('16:00', '16:00'),
              ('17:00', '17:00'),
              ('18:00', '18:00'))

class Agenda(models.Model):

    id_agenda = models.IntegerField(primary_key=True, editable=False)
    medico = models.ForeignKey(Medico,related_name='medico',on_delete=models.CASCADE, null=False, blank=False)
    dia = models.DateField(null=False, blank=False)
    horas = MultiSelectField(choices=MY_CHOICES)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        ordering = ['dia']
        unique_together = ['medico', 'dia']


    def clean(self):
        if self.dia < datetime.now().date():
            raise ValidationError("Impossivel criar agenda para dia passado!")

    def __str__(self):
        return "medico={}, dia={}, horario={}".format(
            self.medico,
            self.dia,
            self.horas)


class Consultas(models.Model):
    id_consulta = models.IntegerField(primary_key=True, editable=False)
    dia = models.DateField(null=False)
    horario = models.ForeignKey(Agenda, null=False, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        unique_together = ['medico', 'dia']

    def __str__(self):
        return "dia={}, horario={}, data_agendamento={}, medico={}".format(
                self.dia,self.horario,self.data_agendamento,self.medico)