from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'democratorrepublican.party.views.homepage'),
    url(r'^party/(?P<party_id>\d+)/$', 'democratorrepublican.party.views.detail'),
    #url(r'^democratorrepublican/', include('democratorrepublican.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

urlpatterns += staticfiles_urlpatterns()
