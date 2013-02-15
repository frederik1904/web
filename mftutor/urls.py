from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mftutor.views.home', name='home'),
    # url(r'^mftutor/', include('mftutor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('news.urls'), name='news'),
    url(r'^news/', include('news.urls')),
    url(r'^', include('page.urls')),
    url(r'^', include('tutor.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^activation/', include('activation.urls')),
    url(r'^email/', include('tutormail.urls')),
)
