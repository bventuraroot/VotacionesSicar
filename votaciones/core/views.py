from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Congregacion
from .serializer import Congregacion_serializer
from django.contrib.auth.models import User  # TODO Tabla User
from rest_framework.authtoken.models import Token  # Todo table Token
import json
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

class congregacionAllView(generics.ListAPIView):
    queryset = Congregacion.objects.all()
    serializer_class = Congregacion_serializer
    permission_classes = (AllowAny,)
    


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def congregacion_crud(request, pk):
    try:
        congregacion = Congregacion.objects.get(pk=pk)
        if request.method == 'GET':
            congregacion_serializer = Congregacion_serializer(congregacion)
            return JsonResponse(congregacion_serializer.data)
        elif request.method == 'POST':
            congregacion_data = JSONParser().parse(request)
            congregacion_serializer = Congregacion_serializer(data=congregacion_data)
            if congregacion_serializer.is_valid():
                congregacion_serializer.save()
                return JsonResponse({'Message': 'Datos del Miembro ingresados con exito'} + congregacion_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(congregacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            congregacion.delete()
            return JsonResponse({'Message': 'Datos del Miembro eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            congregacion_data = JSONParser().parse(request)
            congregacion_serializer = Congregacion_serializer(congregacion, data=congregacion_data)
            if congregacion_serializer.is_valid():
                congregacion_serializer.save()
                return JsonResponse({'Message': 'Datos del Miembro modificados con exito'} + congregacion_serializer.data)
            return JsonResponse(congregacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Congregacion.DoesNotExist:

        return JsonResponse({'message': 'El miembro de la congregacion no existe'}, status=status.HTTP_404_NOT_FOUND)
