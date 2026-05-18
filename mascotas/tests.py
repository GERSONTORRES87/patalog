from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from .models import Mascota, Vacuna, RegistroVacuna


class MascotaModelTest(TestCase):
    def setUp(self):
        self.mascota = Mascota.objects.create(
            nombre='Max',
            especie='perro',
            raza='Labrador',
            fecha_nacimiento=date(2020, 1, 1)
        )

    def test_mascota_str(self):
        self.assertEqual(str(self.mascota), 'Max (Perro)')

    def test_mascota_especie(self):
        self.assertEqual(self.mascota.especie, 'perro')

    def test_mascota_nombre(self):
        self.assertEqual(self.mascota.nombre, 'Max')


class VacunaModelTest(TestCase):
    def setUp(self):
        self.vacuna = Vacuna.objects.create(
            nombre='Rabia',
            especie='ambos',
            frecuencia_meses=12
        )

    def test_vacuna_str(self):
        self.assertEqual(str(self.vacuna), 'Rabia')

    def test_vacuna_frecuencia(self):
        self.assertEqual(self.vacuna.frecuencia_meses, 12)


class RegistroVacunaModelTest(TestCase):
    def setUp(self):
        self.mascota = Mascota.objects.create(nombre='Kira', especie='perro')
        self.vacuna = Vacuna.objects.create(nombre='Parvovirus', especie='perro')
        self.registro = RegistroVacuna.objects.create(
            mascota=self.mascota,
            vacuna=self.vacuna,
            fecha_aplicacion=date.today()
        )

    def test_registro_str(self):
        self.assertIn('Kira', str(self.registro))
        self.assertIn('Parvovirus', str(self.registro))


class MascotaViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.mascota = Mascota.objects.create(nombre='Nala', especie='gato')

    def test_lista_mascotas(self):
        response = self.client.get(reverse('mascotas:lista'))
        self.assertEqual(response.status_code, 200)

    def test_detalle_mascota(self):
        response = self.client.get(reverse('mascotas:detalle', args=[self.mascota.pk]))
        self.assertEqual(response.status_code, 200)

    def test_inicio(self):
        response = self.client.get(reverse('mascotas:inicio'))
        self.assertEqual(response.status_code, 200)
