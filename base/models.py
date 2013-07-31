# coding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

NOMBRE_MAX_LENGTH = 100


class Jugador(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    nombre = models.CharField(max_length = NOMBRE_MAX_LENGTH)
    #equipos = models.ManyToManyField(Equipo, related_name='equipos')

    def __unicode__(self):
        if self.nombre == '':
            return "<Jugador #%s>" % self.id
        return self.nombre

# cuando se crea un usuario, se crea un jugador asociado a ese usuario
def user_post_save(sender, instance, **kwargs):
    jugador, new = Jugador.objects.get_or_create(user=instance)

models.signals.post_save.connect(user_post_save, sender=User)


class Equipo(models.Model):
    nombre = models.CharField(max_length = NOMBRE_MAX_LENGTH)
    jugadores = models.ManyToManyField(Jugador, through='MembresiaEquipo',
                                       related_name='equipos')

    def __unicode__(self):
        return self.nombre

    def agregar_jugador(self, jugador, aprobado=False):
        membresia, created = MembresiaEquipo.objects.get_or_create(
            jugador=jugador, equipo=self)
        membresia.aprobado = aprobado
        membresia.save()
        return membresia, created

    """Obtiene los jugadores con aprobación pendiente"""
    def jugadores_pendientes(self):
        membresias_equipo = self.membresias.all()
        jugadores_pendientes = []
        for membresia in membresias_equipo:
            if membresia.aprobado is not True and membresia.es_admin is False:
                jugadores_pendientes.append(membresia.jugador)
        return jugadores_pendientes


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'jugadores']


class MembresiaEquipo(models.Model):
    jugador = models.ForeignKey(Jugador, related_name='membresia_equipos')
    equipo = models.ForeignKey(Equipo, related_name='membresias')
    aprobado = models.BooleanField(default=False)

    es_admin = models.BooleanField(default=False)
    es_capitan = models.BooleanField(default=False)
    # date_joined = models.DateField()
    # invite_reason = models.CharField(max_length=64)

    class Meta:
        unique_together = ("jugador", "equipo")

    def __unicode__(self):
        return 'El jugador "%s" juega en "%s"' % (self.jugador, self.equipo)

    def save(self, *args, **kwargs):
        membresia = MembresiaEquipo.objects.filter(equipo=self.equipo)
        if not membresia:
            self.aprobado = True
            self.es_admin = True
            self.es_capitan = True
        instance = super(MembresiaEquipo, self).save(*args, **kwargs)
        return instance


class Partido(models.Model):
    equipo1 = models.ForeignKey(Equipo, related_name='equipo1')
    equipo2 = models.ForeignKey(Equipo, related_name='equipo2')
    goles1 = models.IntegerField(default=0)
    goles2 = models.IntegerField(default=0)
    fecha = models.DateTimeField()

    def __unicode__(self):
        return '%s vs %s (%s)' % (self.equipo1, self.equipo2, self.fecha)
