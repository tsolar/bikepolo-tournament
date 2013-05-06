from django.conf.urls import patterns, include, url

from .views import JugadorListView


urlpatterns = patterns('',
                       url(r'^$', 'base.views.equipos_index', name='base_equipos_index'),
                       # url(r'^list/', EquiposListView.as_view(), name='base_equipos_list'),
                       url(r'^solicitar_membresia/$', 'base.views.equipos_solicitar_membresia', name='base_equipos_solicitar_membresia'),
                       url(r'^solicitar_membresia/(?P<equipo>[^/]+)/done$', 'base.views.equipos_solicitar_membresia_done', name='base_equipos_solicitar_membresia_done'),
)
