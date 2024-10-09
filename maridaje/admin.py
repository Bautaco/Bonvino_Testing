from django.contrib import admin
from .models import Vino, Comida, Maridaje

# Register your models here.
admin.site.register(Vino)
admin.site.register(Comida)
admin.site.register(Maridaje)
