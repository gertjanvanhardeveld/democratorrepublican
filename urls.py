from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'democratorrepublican.party.views.homepage'),
    url(r'^about/$', 'democratorrepublican.party.views.about'),
    url(r'^maps/$', 'democratorrepublican.party.views.maps'),
    url(r'^mobile/$', 'democratorrepublican.party.views.mobile'),
    url(r'^democrats/$', 'democratorrepublican.party.views.democrats'),
    url(r'^republicans/$', 'democratorrepublican.party.views.republicans'),
    url(r'^otherparties/$', 'democratorrepublican.party.views.otherparties'),
    url(r'^party/(?P<party_id>\d+)/$', 'democratorrepublican.party.views.detail'),
    #url(r'^democratorrepublican/', include('democratorrepublican.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/create/$', 'democratorrepublican.party.views.create'),
)



urlpatterns += staticfiles_urlpatterns()
