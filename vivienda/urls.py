"""vivienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from vivienda.views import Inicio, PaginaPrincipal, Custom404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^solicitudes/', include('solicitudes.urls',namespace="solicitudes")),
    url(r'^sector_zona/', include('sector_zona.urls',namespace="sector_zona")),
    url(r'^inicio/$', Inicio.as_view(), name="inicio"),

    url(r'^$', PaginaPrincipal.as_view(), name="homepage"),
    url(r'^usuario/', include('usuario.urls', namespace="usuario"))
]

handler404 = Custom404.as_view()
