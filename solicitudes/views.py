from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, CreateView, DeleteView, \
    UpdateView, DetailView, TemplateView
from django.core.urlresolvers import reverse_lazy
from usuario.models import Usuario
from solicitudes import forms, models
from django.utils import timezone
# django paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# method or
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

# Create your views here.


class SolicitanteListView(LoginRequiredMixin, ListView):
    model = Usuario
    paginate_by = settings.PAGINATE
    template_name = 'solicitudes/solicitante_list.html'

    def get_context_data(self, **kwargs):
        context = super(SolicitanteListView, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        result = None
        if q:
            result = self.model.objects.filter(
                Q(cedula__contains=q) | Q(
                    nombre__contains=q) | Q(apellido__contains=q),
                is_solicitante=True).exclude(username=self.request.user.username).order_by('-created_at')
        else:
            result = self.model.objects.filter(is_solicitante=True).exclude(
                username=self.request.user.username).order_by('-created_at')

        paginator = Paginator(result, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)
        context['object_list'] = object_list
        return context


class SolicitanteCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    form_class = forms.SolicitanteForm
    template_name = 'solicitudes/solicitante_form.html'

    def form_valid(self, form):
        _object = form.save(commit=False)
        _object.username = _object.cedula
        _object.is_solicitante = True
        self.object = _object.save()
        return super(SolicitanteCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('solicitudes:detail_solicitante', args=(self.object.pk,))


class SolicitanteDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'solicitudes/solicitante_detail.html'

    def get_object(self):
        object = self.model.objects.filter(
            pk=self.kwargs.get('pk')).exclude(
                pk=self.request.user.pk).first()
        if object:
            return object
        raise Http404


class SolicitanteDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('solicitudes:list_solicitante')
    template_name = 'solicitudes/solicitante_confirm_delete.html'


class SolicitanteUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = forms.SolicitanteForm
    template_name = 'solicitudes/solicitante_form.html'

    def get_context_data(self, **kwargs):
        context = super(SolicitanteUpdateView, self).get_context_data(**kwargs)
        context['user'] = {"exist": True, "user": self.object}
        return context

    def get_success_url(self):
        return reverse_lazy('solicitudes:detail_solicitante', args=(self.object.pk,))


# Solicitudes


class SolicitudListView(LoginRequiredMixin, ListView):
    model = models.Solicitud


class SolicitudDetailView(LoginRequiredMixin, DetailView):
    model = models.Solicitud


class SolicitudCreateView(LoginRequiredMixin, CreateView):
    model = models.Solicitud
    form_class = forms.SolicitudForm

    def get_success_url(self):
        return reverse_lazy('solicitudes:detail', args=(self.object.pk,))


class SolicitudUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Solicitud
    form_class = forms.SolicitudForm

    def get_success_url(self):
        return reverse_lazy('solicitudes:detail', args=(self.object.pk,))


class SolicitudDeleteView(DeleteView):
    model = models.Solicitud
    success_url = reverse_lazy('solicitudes:list')
