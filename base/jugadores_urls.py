from django.conf.urls import patterns, include, url

from .views import JugadorListView


urlpatterns = patterns('',
                       url(r'^$', 'base.views.jugadores_index', name='base_jugadores_index'),
                       url(r'^list/', JugadorListView.as_view(), name='base_jugadores_list'),                      
)
