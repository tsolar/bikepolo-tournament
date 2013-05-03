from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Jugador

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
