from rest_framework import serializers
from .models import Vino, Comida, Maridaje

class VinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vino
        fields = '__all__'

class ComidaSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = '__all__'

class MaridajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maridaje
        fields = '__all__'
