from django.db import models


class Mascota(models.Model):
    ESPECIE_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
    ]
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_especie_display()})"

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        ordering = ['nombre']


class Vacuna(models.Model):
    ESPECIE_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ambos', 'Ambos'),
    ]
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES, default='ambos')
    frecuencia_meses = models.IntegerField(help_text="Frecuencia en meses", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Vacuna"
        verbose_name_plural = "Vacunas"
        ordering = ['nombre']


class RegistroVacuna(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='vacunas')
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateField()
    proxima_dosis = models.DateField(null=True, blank=True)
    veterinario = models.CharField(max_length=200, blank=True)
    notas = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mascota.nombre} - {self.vacuna.nombre} ({self.fecha_aplicacion})"

    class Meta:
        verbose_name = "Registro de Vacuna"
        verbose_name_plural = "Registros de Vacunas"
        ordering = ['-fecha_aplicacion']
