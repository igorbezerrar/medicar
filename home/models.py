from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
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



HORARIOS = (('08:00', '08:00'),
            ('09:00', '09:00'),
            ('10:00', '10:00'),
            ('11:00', '11:00'),
            ('12:00', '12:00'),
            ('13:00', '13:00'),
            ('14:00', '14:00'),
            ('15:00', '15:00'),
            ('16:00', '16:00'),
            ('17:00', '17:00'),
            ('18:00', '18:00'),
            ('19:00', '19:00'),
            ('20:00', '20:00'),
            ('21:00', '21:00'),
            ('22:00', '22:00'),
            ('23:00', '23:00'),)

class Agenda(models.Model):

    id_agenda = models.IntegerField(primary_key=True, editable=False)
    medico = models.ForeignKey(Medico, related_name='medico',on_delete=models.CASCADE, null=False, blank=False)
    dia = models.DateField(null=False, blank=False)
    horarios = MultiSelectField(choices=HORARIOS)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        ordering = ['dia']
        unique_together = ['medico', 'dia']
        constraints = [
            models.CheckConstraint(check=models.Q(dia__gte=timezone.now()), name='dia__gte'),
        ]

    def clean(self):
        if self.dia < datetime.now().date():
            raise ValidationError("Impossivel criar agenda para dia passado!")

    def __str__(self):
        return "medico={}, dia={}, horarios={}".format(
            self.medico,
            self.dia,
            self.horarios)


class Consultas(models.Model):
    id_consulta = models.IntegerField(primary_key=True, editable=False)
    dia = models.DateField(null=False)
    horario = models.TimeField(null=False)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        unique_together = ['dia', 'horario', 'usuario']


    def __str__(self):
        return "dia={}, horario={}, data_agendamento={}, medico={}".format(
                self.dia,self.horario,self.data_agendamento,self.medico)