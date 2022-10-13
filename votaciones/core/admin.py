from django.contrib import admin
from .models import Congregacion, Continentes, Departamentos, Gastos, Lideres, Ministerios, Paises, Votaciones, VotacionesAdmin


class ItemAdminCongre(admin.ModelAdmin):
    list_display = ("nombre_completo","code", "activo", "municipio", "departamento")
    list_editable = ("activo",)
    
#admin.site.register([Congregacion, Continentes, Departamentos, Gastos, Lideres, Ministerios, Paises, Votaciones, VotacionesAdmin])
admin.site.register(Congregacion, ItemAdminCongre)

class ItemAdminContinente(admin.ModelAdmin):
    list_display = ("nombre",)
admin.site.register(Continentes, ItemAdminContinente)

class ItemAdminLideres(admin.ModelAdmin):
    list_display = ("code_name", "Ministerio",)
admin.site.register(Lideres, ItemAdminLideres)

admin.site.register([Departamentos, Gastos, Ministerios, Paises, Votaciones, VotacionesAdmin])
