from django.contrib import admin
from .models import Mascota, Vacuna, RegistroVacuna


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'raza', 'fecha_nacimiento', 'creado']
    list_filter = ['especie']
    search_fields = ['nombre', 'raza']


@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'frecuencia_meses']
    list_filter = ['especie']
    search_fields = ['nombre']


@admin.register(RegistroVacuna)
class RegistroVacunaAdmin(admin.ModelAdmin):
    list_display = ['mascota', 'vacuna', 'fecha_aplicacion', 'proxima_dosis', 'veterinario']
    list_filter = ['vacuna', 'mascota__especie']
    search_fields = ['mascota__nombre', 'vacuna__nombre', 'veterinario']
    date_hierarchy = 'fecha_aplicacion'
