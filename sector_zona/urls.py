from django.conf.urls import url
from sector_zona.views import *

urlpatterns = [
    url(r'^api/municipio/(?P<pk>[-\ \w]+)/$', ApiMunicipioView.as_view(), name="api_municipio"),
    url(r'^api/parroquia/(?P<pk>[-\ \w]+)/$', ApiParroquiaView.as_view(), name="api_parroquia"),
]
