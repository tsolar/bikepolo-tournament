from django.contrib.auth.models import User
from django.test import TestCase

from .models import Equipo, Jugador, MembresiaEquipo


def create_user(**kwargs):
    defaults = {
        'username': 'user1',
    }
    defaults.update(kwargs)

    return User.objects.create(**defaults)


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


class JugadorTest(TestCase):
    def test_usuario_post_save(self):
        user = create_user()
        self.assertIsNotNone(user.jugador)
        jugador = user.jugador
        self.assertIsInstance(jugador, Jugador)

    
class EquipoTest(TestCase):
    def setUp(self):
        self.equipo1 = create_equipo()
        self.jugador1 = create_jugador()

    def test_agregar_jugador_aprobado_false(self):
        membresia, created = self.equipo1.agregar_jugador(
            jugador=self.jugador1)
        self.assertTrue(created)
        self.assertEqual(MembresiaEquipo.objects.all()[0], membresia)
        self.assertEqual(membresia.jugador.nombre, 'jugador 1')
        self.assertEqual(membresia.equipo.nombre, 'Super equipo')
        self.assertFalse(membresia.aprobado)
        self.assertTrue(membresia.es_capitan)  # True porque es el primero
        self.assertTrue(membresia.es_admin)  # True porque es el primero

    def test_agregar_jugador_aprobado_true(self):
        membresia, created = self.equipo1.agregar_jugador(
            jugador=self.jugador1, aprobado=True)
        self.assertTrue(created)
        self.assertEqual(MembresiaEquipo.objects.all()[0], membresia)
        self.assertEqual(membresia.jugador.nombre, 'jugador 1')
        self.assertEqual(membresia.equipo.nombre, 'Super equipo')
        self.assertTrue(membresia.aprobado)
        self.assertTrue(membresia.es_capitan)
        self.assertTrue(membresia.es_admin)

    def test_agregar_jugador_membresia_existente(self):
        membresia1 = create_membresia_equipo(
            jugador=self.jugador1, equipo=self.equipo1
        )
        membresia, created = self.equipo1.agregar_jugador(
            jugador=self.jugador1, aprobado=True)
        self.assertFalse(created)
        self.assertEqual(MembresiaEquipo.objects.all()[0], membresia)
        self.assertEqual(membresia.jugador.nombre, 'jugador 1')
        self.assertEqual(membresia.equipo.nombre, 'Super equipo')
        self.assertTrue(membresia.aprobado)
        self.assertEqual(membresia1.es_admin, membresia.es_admin)
        self.assertEqual(membresia1.es_capitan, membresia.es_capitan)


class MembresiaEquipoTest(TestCase):
    def setUp(self):
        self.equipo = create_equipo()


    def test_create_membresia(self):
        membresia1 = create_membresia_equipo(equipo=self.equipo)
        self.assertTrue(membresia1.es_admin)
        self.assertTrue(membresia1.es_capitan)

        membresia2 = create_membresia_equipo(equipo=self.equipo)
        self.assertFalse(membresia2.es_admin)
        self.assertFalse(membresia2.es_capitan)
