from django.conf.urls import url
from usuario.views import UsuarioListView, UsuarioCreateView, \
                            UsuarioUpdateView, UsuarioDetailView, \
                            UsuarioDeleteView, UsuarioAdminDetailView, \
                            UsuarioAdminUpdateView

urlpatterns = [
    url(r'^$', UsuarioListView.as_view(), name="list"),
    url(r'register/$', UsuarioCreateView.as_view(), name="register"),
    url(r'^(?P<pk>[-\ \w]+)/detail/$',
        UsuarioDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[-\ \w]+)/update/$',
        UsuarioUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[-\ \w]+)/delete/$',
        UsuarioDeleteView.as_view(), name='delete'),
    
    ## Profile
    url(r'^detail/$',
        UsuarioAdminDetailView.as_view(), name='detail_profile'),
    url(r'^update/$',
        UsuarioAdminUpdateView.as_view(), name='update_profile'),
]
