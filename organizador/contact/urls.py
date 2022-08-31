
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='contact'),#sin paramtro opcional
   path('<letter>', views.index, name='contact'),#con parametro opcional
   #como estamos usando parametros opcionales debemos poner doble url para que funcione
   path('view/<int:id>', views.view, name='contact_view'),
   path('edit/<int:id>', views.edit, name='contact_edit'),
   path('create/', views.create, name='contact_create'),
   path('delete/<int:id>', views.delete, name='contact_delete'),
]