from django.contrib import admin
from .models import \
    Equipo, \
    Jugador, \
    MembresiaEquipo


admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(MembresiaEquipo)

