from django.test import TestCase

from .models import Equipo, Jugador, MembresiaEquipo


def create_equipo(**kwargs):
    defaults = {
        'nombre': 'Super equipo',
    }
    defaults.update(kwargs)
    
    return Equipo.objects.create(**defaults)

def create_jugador(**kwargs):
    defaults = {
        'nombre': 'jugador 1',
    }
    defaults.update(kwargs)
    
    return Jugador.objects.create(**defaults)

def create_membresia_equipo(**kwargs):
    defaults = {
        'jugador': create_jugador(),
        'equipo': create_equipo(),
    }    
    defaults.update(kwargs)

    return MembresiaEquipo.objects.create(**defaults)
    
    
class EquipoTest(TestCase):
    def setUp(self):
        self.equipo1 = create_equipo()
        self.jugador1 = create_jugador()

    def test_agregar_jugador(self):
        membresia, created = MembresiaEquipo.objects.get_or_create(
            jugador=self.jugador1, equipo=self.equipo1)
        self.assertTrue(created)
        self.assertEqual(MembresiaEquipo.objects.all()[0], membresia)
        self.assertEqual(membresia.jugador.nombre, 'jugador 1')
        self.assertEqual(membresia.equipo.nombre, 'Super equipo')
        self.assertFalse(membresia.aprobado)

    def test_agregar_jugador_membresia_existente(self):
        membresia1 = create_membresia_equipo(
            jugador=self.jugador1, equipo=self.equipo1
        )
        membresia, created = MembresiaEquipo.objects.get_or_create(
            jugador=self.jugador1, equipo=self.equipo1)
        self.assertFalse(created)
        self.assertEqual(MembresiaEquipo.objects.all()[0], membresia)
        self.assertEqual(membresia.jugador.nombre, 'jugador 1')
        self.assertEqual(membresia.equipo.nombre, 'Super equipo')
        self.assertFalse(membresia.aprobado)
