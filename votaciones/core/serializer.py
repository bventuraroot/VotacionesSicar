from dataclasses import fields
from rest_framework import serializers
from .models import Congregacion

class Congregacion_serializer(serializers.ModelSerializer):
    class Meta:
        model = Congregacion
        fields = '__all__'