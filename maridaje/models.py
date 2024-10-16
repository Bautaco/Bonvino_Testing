from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.CharField(max_length=100)
    varietal = models.CharField(max_length=50)
    region = models.CharField(max_length=100)

    def clean(self):
        if not self.nombre:
            raise ValidationError('El campo nombre no puede estar vacío.')
        if not self.region:
            raise ValidationError('El campo region no puede estar vacío.')
    
    def __str__(self):
        return self.nombre

class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def clean(self):
        if not self.nombre:
            raise ValidationError('El campo nombre no puede estar vacío.')

    def __str__(self):
        return self.nombre

class Maridaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='maridajes/', null=True, blank=True)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)

    def clean(self):
        if not self.nombre:
            raise ValidationError('El campo nombre no puede estar vacío.')
        if not self.descripcion:
            raise ValidationError('El campo descripcion no puede estar vacío.')

    def __str__(self):
        return self.nombre
