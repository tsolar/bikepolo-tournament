from django.conf.urls import patterns, include, url

from .views import JugadorListView


urlpatterns = patterns('',
                       url(r'^$', 'base.views.equipos_index', name='base_equipos_index'),
                       # url(r'^list/', EquiposListView.as_view(), name='base_equipos_list'),
                       url(r'^crear/', 'base.views.equipos_crear', name='base_equipos_crear'),
                       url(r'^membresia/solicitar/$', 'base.views.equipos_solicitar_membresia', name='base_equipos_solicitar_membresia'),
                       url(r'^membresia/solicitar/(?P<equipo>[^/]+)/done$', 'base.views.equipos_solicitar_membresia_done', name='base_equipos_solicitar_membresia_done'),
                       url(r'^membresia/admin/$', 'base.views.equipos_administrar_membresia_index', name='base_equipos_administrar_membresia_index'),
                       url(r'^membresia/admin/(?P<equipo_id>[^/]+)/$', 'base.views.equipos_administrar_membresia_equipo', name='base_equipos_administrar_membresia_equipo'),
                       url(r'^membresia/aprobar$', 'base.views.equipos_aprobar_membresia', name='base_equipos_aprobar_membresia'),
                       url(r'^membresia/borrar/$', 'base.views.equipos_borrar_membresia', name='base_equipos_borrar_membresia'),
                       url(r'^lista_jugadores/$', 'base.views.equipos_get_lista_jugadores', name='base_equipos_get_lista_jugadores_equipo'),
)
