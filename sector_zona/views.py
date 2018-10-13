from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json
from django.views.generic import ListView, CreateView, DeleteView, \
    UpdateView, DetailView, TemplateView, View
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from sector_zona.models import Estado, Municipio, Parroquia
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ApiMunicipioView(LoginRequiredMixin, View):
    model = Municipio

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        data = self.model.objects.filter(estado__pk=pk)
        data = serializers.serialize(
            "json", data)
        return JsonResponse(data, safe=False)


class ApiParroquiaView(LoginRequiredMixin, View):
    model = Parroquia

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        data = self.model.objects.filter(municipio__pk=pk)
        data = serializers.serialize(
            "json", data)
        return JsonResponse(data, safe=False)
