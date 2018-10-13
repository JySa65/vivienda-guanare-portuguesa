from django.contrib import admin
from sector_zona.models import Estado, Parroquia, Municipio
# Register your models here.

admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Parroquia)