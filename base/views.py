from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.utils import timezone

from .forms import SolicitarMembresiaForm
from .models import Jugador, Equipo


def index(request):
    return HttpResponse("holaaaa!")


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