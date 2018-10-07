from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, CreateView, DeleteView, \
    UpdateView, DetailView, TemplateView
from django.core.urlresolvers import reverse_lazy
from usuario import models, forms
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


class UsuarioListView(LoginRequiredMixin, ListView):
    model = models.Usuario
    paginate_by = settings.PAGINATE

    def get_context_data(self, **kwargs):
        context = super(UsuarioListView, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        result = None
        if q:
            result = self.model.objects.filter(
                Q(cedula__contains=q) | Q(
                    nombre__contains=q) | Q(apellido__contains=q)
            ).exclude(username=self.request.user.username).order_by('-created_at')
        else:
            result = self.model.objects.all().exclude(
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


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = models.Usuario

    def get_object(self):
        object = self.model.objects.filter(
            pk=self.kwargs.get('pk')).exclude(
                pk=self.request.user.pk).first()
        if object:
            return object
        raise Http404


class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = models.Usuario
    form_class = forms.UsuarioForm

    def form_valid(self, form):
        _object = form.save(commit=False)
        _object.username = _object.cedula
        self.object = _object.save()
        return super(UsuarioCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('usuario:detail', args=(self.object.pk,))


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Usuario
    form_class = forms.UsuarioActualizarForm

    def get_context_data(self, **kwargs):
        context = super(UsuarioUpdateView, self).get_context_data(**kwargs)
        context['user'] = {"exist": True, "user": self.object}
        return context

    def get_success_url(self):
        return reverse_lazy('usuario:detail', args=(self.object.pk,))


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Usuario
    success_url = reverse_lazy('usuario:list')


class UsuarioAdminDetailView(LoginRequiredMixin, DetailView):
    model = models.Usuario

    def get_object(self):
        user = self.request.user.pk
        object = get_object_or_404(self.model, pk=user)
        return object

    def get_context_data(self, **kwargs):
        context = super(UsuarioAdminDetailView,
                        self).get_context_data(**kwargs)
        context['profile'] = True
        return context


class UsuarioAdminUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Usuario
    form_class = forms.UsuarioForm

    def get_object(self):
        user = self.request.user.pk
        object = get_object_or_404(self.model, pk=user)
        return object

    def get_context_data(self, **kwargs):
        context = super(UsuarioAdminUpdateView,
                        self).get_context_data(**kwargs)
        context['user'] = {"exist": True, "user": self.object}
        context['profile'] = True
        return context

    def get_success_url(self):
        return reverse_lazy('usuario:detail_profile')
