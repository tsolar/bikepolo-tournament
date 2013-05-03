# coding: utf-8
from django.contrib.auth.models import User
from django.db import models

NOMBRE_MAX_LENGTH = 100


class Jugador(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    nombre = models.CharField(max_length = NOMBRE_MAX_LENGTH)
    #equipos = models.ManyToManyField(Equipo, related_name='equipos')

    def __unicode__(self):
        return self.nombre


class Equipo(models.Model):
    nombre = models.CharField(max_length = NOMBRE_MAX_LENGTH)
    jugadores = models.ManyToManyField(Jugador, through='MembresiaEquipo', related_name='equipos')

    def __unicode__(self):
        return self.nombre

    def agregar_jugador(self, jugador, aprobado=False):
        membresia, created = MembresiaEquipo.objects.get_or_create(jugador=jugador, equipo=self)
        membresia.aprobado = aprobado
        membresia.save()

        
class MembresiaEquipo(models.Model):
    jugador = models.ForeignKey(Jugador, related_name='membresia_equipos')
    equipo = models.ForeignKey(Equipo, related_name='membresias')
    aprobado = models.BooleanField(default=False)
    # date_joined = models.DateField()
    # invite_reason = models.CharField(max_length=64)  

    class Meta:
        unique_together = ("jugador", "equipo")

    def __unicode__(self):
        return 'El jugador "%s" juega en "%s"' % (self.jugador, self.equipo)
    

class Partido(models.Model):
    equipo1 = models.ForeignKey(Equipo, related_name='equipo1')
    equipo2 = models.ForeignKey(Equipo, related_name='equipo2')
    goles1 = models.IntegerField(default=0)
    goles2 = models.IntegerField(default=0)
    fecha = models.DateTimeField()

    def __unicode__(self):
        return '%s vs %s (%s)' % (self.equipo1, self.equipo2, self.fecha)

