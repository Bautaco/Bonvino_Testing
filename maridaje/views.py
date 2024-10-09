from rest_framework import viewsets

from maridaje.serializer import ComidaSerializaer, MaridajeSerializer, VinoSerializer
from .models import Vino, Comida, Maridaje


# Create your views here.
class VinoView(viewsets.ModelViewSet):
    serializer_class = VinoSerializer
    queryset = Vino.objects.all()

class ComidaView(viewsets.ModelViewSet):
    serializer_class = ComidaSerializaer
    queryset = Comida.objects.all()

class MaridajeView(viewsets.ModelViewSet):
    serializer_class = MaridajeSerializer
    queryset = Maridaje.objects.all()



