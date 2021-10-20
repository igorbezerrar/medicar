from django.contrib import admin

from .models import Especialidade, Medico, Agenda, Consultas


# @admin.register(Usuario)
# class UsuarioAdmin(admin.ModelAdmin):
#     list_display = ('user', 'nome', 'senha')


@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id_especialidade','nome')


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email', 'telefone', 'especialidade')


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id_agenda', 'medico', 'dia', 'horarios')


@admin.register(Consultas)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id_consulta', 'dia', 'horario','data_agendamento', 'medico', 'usuario')


