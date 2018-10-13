from django.views.generic import TemplateView
from usuario.models import Usuario
from solicitudes.models import Solicitud
from django.contrib.auth.mixins import LoginRequiredMixin


class Inicio(LoginRequiredMixin, TemplateView):
    template_name = "inicio/index.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['solicitante'] = Usuario.objects.filter(is_solicitante=True).exclude(
            pk=self.request.user.pk).count()
        context['solicitudes'] = Solicitud.objects.all().count()
        return context


class PaginaPrincipal(TemplateView):
    template_name = "inicio/pagina_principal.html"


class Custom404(TemplateView):
    template_name = "inicio/404.html"
