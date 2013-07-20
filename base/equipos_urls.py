from django.conf.urls import patterns, include, url

from .views import JugadorListView


urlpatterns = patterns('',
                       url(r'^$', 'base.views.equipos_index', name='base_equipos_index'),
                       # url(r'^list/', EquiposListView.as_view(), name='base_equipos_list'),
                       url(r'^crear/', 'base.views.equipos_crear', name='base_equipos_crear'),
                       url(r'^crear/done$', 'base.views.equipos_crear', name='base_equipos_crear'),
                       url(r'^solicitar_membresia/$', 'base.views.equipos_solicitar_membresia', name='base_equipos_solicitar_membresia'),
                       url(r'^solicitar_membresia/(?P<equipo>[^/]+)/done$', 'base.views.equipos_solicitar_membresia_done', name='base_equipos_solicitar_membresia_done'),
                       url(r'^administrar_membresia/$', 'base.views.equipos_administrar_membresia_index', name='base_equipos_administrar_membresia_index'),
                       url(r'^administrar_membresia/(?P<equipo>[^/]+)/$', 'base.views.equipos_administrar_membresia_equipo', name='base_equipos_administrar_membresia_equipo'),
                       url(r'^aprobar_membresia/$', 'base.views.equipos_aprobar_membresia', name='base_equipos_aprobar_membresia'),
)
