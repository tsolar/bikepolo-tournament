from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from base.views import JugadorListView


admin.autodiscover()


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bikepolo_tournament.views.home', name='home'),
                       # url(r'^bikepolo_tournament/', include('bikepolo_tournament.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       
                       url(r'', include('social_auth.urls')),

                       url(r'^accounts/', include('accounts.urls')),
                       
                       url(r'^$', 'base.views.index', name='base_index'),
                       url(r'^logout/$',
                           'django.contrib.auth.views.logout',
                           {'next_page': '/'}, name='logout'),
                       # url(r'^equipos$', 'base.views.equipos_index', name='base_equipos_index'),
                       # url(r'^jugadores$', 'base.views.jugadores_index', name='base_jugadores_index'),
                       # url(r'^jugadores/list/$', JugadorListView.as_view(), name='base_jugadores_list'),
                       url(r'^jugadores/', include('base.jugadores_urls')),
                       
)
