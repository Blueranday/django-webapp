from django.contrib import admin
from .models import Proyecto, Tarea

# Personalización de cómo se ve Proyecto en el panel admin
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_creacion')
    list_filter = ('usuario',)
    search_fields = ('nombre',)

# Personalización de cómo se ve Tarea en el panel admin
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proyecto', 'estado', 'fecha_limite')
    list_filter = ('estado', 'proyecto')
    search_fields = ('titulo',)