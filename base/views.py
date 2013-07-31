# coding: utf-8
import json
from pprint import pprint

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.list import ListView
from django.utils import timezone

from .forms import SolicitarMembresiaForm
from .models import Jugador, Equipo, EquipoForm, MembresiaEquipo


def index(request):
    return render(request, 'index.html')


def equipos_index(request):
    return HttpResponse("equipos holaaaa!")


def jugadores_index(request):
    return HttpResponse("jugadores holaaaa!")


class JugadorListView(ListView):

    model = Jugador

    def get_context_data(self, **kwargs):
        context = super(JugadorListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def equipos_solicitar_membresia(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SolicitarMembresiaForm(
            request.POST)  # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            if '_auth_user_id' not in request.session:
                return redirect(reverse('base_index'))
            else:
                user_pk = request.session['_auth_user_id']
            user = User.objects.get(pk=user_pk)
            equipo = form.cleaned_data.get('equipo')
            membresia, created = equipo.agregar_jugador(user.jugador)
            return HttpResponse(created)
            return redirect(
                reverse('base_equipos_solicitar_membresia_done',
                        # kwargs={'equipo':equipo}
                )
            )
    else:
        form = SolicitarMembresiaForm() # An unbound form

    return render(request, 'equipos/solicitar_membresia.html', {
        'form': form,
    })


def equipos_solicitar_membresia_done(request, equipo):
    return render(request, 'equipos/solicitar_membresia_done.html', {
        # 'jugador': jugador,
        'equipo': equipo,
    })


def equipos_administrar_membresia_index(request):
    user = request.user
    membresia_equipos = user.jugador.membresia_equipos.all()

    equipos_administrados = []
    for membresia in membresia_equipos:
        equipos_administrados.append(membresia.equipo)

    return render(request, 'equipos/administrar_membresia.html', {
        # 'jugador': jugador,
        # 'equipos': equipos,
        'equipos_administrados': equipos_administrados,
    })


def equipos_administrar_membresia_equipo(request, equipo_id):
    # TODO: no poder borrarme yo mismo
    user = request.user
    equipo = Equipo.objects.get(id=equipo_id)

    return render(request, 'equipos/administrar_membresia_equipo.html', {
        'equipo': equipo,
    })


def equipos_aprobar_membresia(request):
    """"""
    jugador = request.POST['jugador_id']
    equipo = request.POST['equipo_id']
    membresia_equipo = MembresiaEquipo.objects.get(equipo=equipo,
                                                      jugador=jugador)
    membresia_equipo.aprobado = True
    membresia_equipo.save()
    json_response = json.dumps(membresia_equipo.aprobado)
    return HttpResponse(json_response, mimetype='application/json')


def equipos_crear(request):
    if request.method == 'POST': # If the form has been submitted...
        form = EquipoForm(
            request.POST)  # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            if '_auth_user_id' not in request.session:
                return redirect(reverse('base_index'))
            else:
                user_pk = request.session['_auth_user_id']
            user = User.objects.get(pk=user_pk)
            nombre_equipo = form.cleaned_data.get('nombre')

            equipo, created = \
                Equipo.objects.get_or_create(nombre=nombre_equipo)

            if created is True:
                equipo.agregar_jugador(user.jugador, aprobado=True)

            jugadores = form.cleaned_data.get('jugadores')
            for jugador in jugadores:
                equipo.agregar_jugador(jugador, aprobado=True)
                # enviar invitación en vez de?
            return redirect(
                reverse('base_equipo_detail',
                        kwargs={'equipo':equipo}
                )
            )
    else:
        form = EquipoForm() # An unbound form

    return render(request, 'equipos/crear.html', {
        'form': form,
    })


def equipo_detail(request, equipo_nombre, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    jugadores = equipo.jugadores.filter(membresia_equipos__aprobado=True)
    return render(request, 'equipos/detail.html', {
        'equipo': equipo,
        'jugadores': jugadores,
    })


def equipos_get_lista_jugadores(request):
    equipo_id = request.POST['equipo_id']
    equipo = Equipo.objects.get(id=equipo_id)
    jugadores_pendientes = equipo.jugadores.filter(
        membresia_equipos__aprobado=False)
    jugadores = equipo.jugadores.filter(membresia_equipos__aprobado=True)

    return render(request, 'equipos/lista_jugadores.html', {
        'equipo': equipo,
        'jugadores': jugadores,
        'jugadores_pendientes': jugadores_pendientes,
    })