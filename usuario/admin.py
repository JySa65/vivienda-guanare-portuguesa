from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario
from django.utils.translation import ugettext, ugettext_lazy as _
# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('ci', 'nombre', 'apellido')
    fieldsets = (
        (None, {
            'fields': (
                'username', 'password'
            ),
        }),

        (_('Personal Info'), {
            'classes': ('wide',),
            'fields': ('tipo_cedula', 'cedula', 'nombre',
                       'apellido', 'telefono', 'fecha_nacimiento', 'correo', 'direccion',),
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions', 
                                       'is_trabajador', 'is_solicitante')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'tipo_cedula', 'cedula', 'nombre',
                       'apellido', 'password1', 'password2'),
        }),
    )

    def ci(self, obj):
        return '{}-{}'.format(
            obj.tipo_cedula, obj.cedula)
