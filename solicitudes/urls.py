from django.conf.urls import url
from solicitudes.views import *

urlpatterns = [
    #-------------------solicitante----------#

    url(r'^solicitante$', SolicitanteListView.as_view(), name="list_solicitante"),
    url(r'solicitante/registrar/$',
        SolicitanteCreateView.as_view(), name="register_solicitante"),
    url(r'^solicitante/(?P<pk>[-\ \w]+)/detail/$',
        SolicitanteDetailView.as_view(), name='detail_solicitante'),
    url(r'^solicitante/(?P<pk>[-\ \w]+)/delete/$',
        SolicitanteDeleteView.as_view(), name='delete_solicitante'),
    url(r'^solicitante/(?P<pk>[-\ \w]+)/update/$',
        SolicitanteUpdateView.as_view(), name='update_solicitante'),

    #--------------------solicitudes------------------#

    url(r'^$', SolicitudListView.as_view(), name="list"),
    url(r'^registrar/$', SolicitudCreateView.as_view(), name="registrar"),
    url(r'^(?P<pk>[-\ \w]+)/detail/$',
        SolicitudDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[-\ \w]+)/update/$',
        SolicitudUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[-\ \w]+)/delete/$',
        SolicitudDeleteView.as_view(), name='delete'),
]
