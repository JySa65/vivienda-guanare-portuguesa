from django.views.generic import TemplateView
from usuario.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin


class Inicio(LoginRequiredMixin, TemplateView):
    template_name = "inicio/index.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.all().exclude(
            pk=self.request.user.pk).count()
        return context


class PaginaPrincipal(TemplateView):
    template_name = "inicio/pagina_principal.html"
