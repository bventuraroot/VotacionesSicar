from django.urls import path
from .views import congregacionAllView, congregacion_crud

urlpatterns = [
     path('api/listahermanos', congregacionAllView.as_view()),
     path('api/listahermanos/<pk>', congregacion_crud),
]
