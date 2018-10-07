from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils import timezone
import datetime
# Create your models here.


class UsuarioManager(BaseUserManager):

    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Usuario debe tener un usuario valido.')
        account = self.model(
            username=self.model.normalize_username(username)
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)
        account.is_superuser = True
        account.is_staff = True
        account.save()
        return account


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigIntegerField(primary_key = True)
    username = models.CharField(_('username'),
                                max_length=40, null=False, unique=True)
    tipo_cedula = models.CharField(max_length=1, choices=(('V', 'V'), ('E', 'E')))
    cedula = models.CharField(unique=True, blank=True, null=True, max_length=8)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(blank=True, null=True, max_length=11)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=9999, blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.cedula)


    def get_full_name(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def get_short_name(self):
        return self.nombre

    def edad(self):
        if self.fecha_nacimiento:
            return int((datetime.datetime.now().date() - self.fecha_nacimiento).days / 365.25)
        return 0
    
    def ci(self):
        return '{}-{}'.format(self.tipo_cedula, self.cedula)