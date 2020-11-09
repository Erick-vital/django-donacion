from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('cargo/', views.cargo, name='cargo'),
    path('exito/<str:args>/', views.exito_vista, name='exito')
]
