from django.contrib import admin
from Maridaje_App.models import Maridaje, Vino, Comida

# Register your models here.
@admin.register(Maridaje)
class MaridajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'vino', 'comida')
    search_fields = ('nombre', 'vino__nombre', 'comida__nombre')

@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'bodega', 'varietal', 'region')
    search_fields = ('nombre', 'bodega', 'varietal', 'region')

@admin.register(Comida)
class ComidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)