from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       
                       # url(r'^$', 'accounts.views.index', name='accounts_index'),
                       url(r'^profile/', 'accounts.views.profile', name='accounts_profile'),
                       
)
