from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^procesar_documentos/', include('procesar_documentos.foo.urls')),
    
    
    url(r'^$', 'documentos.views.home', name='home'),
    url(r'^documentos/', 'documentos.views.home', name='home'),
    url(r'^procesar/(\d)', 'documentos.views.procesar', name='procesar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
