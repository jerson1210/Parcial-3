from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('ver/<codigo>',views.ver),
    path('registrarNota/',views.registrarNota),
    path('borrar/<codigo>',views.borrar),
    path('edicion/<codigo>',views.edicion),
    path('editarNota/',views.editarNota),
    path('registrar/',views.registrar)
]