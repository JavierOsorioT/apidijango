"""API9ISC22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import *
#from api.views import Hambuegesas2
from api import views
#from . import views  # Importa todas las vistas de tu aplicación actual

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.SignupPage, name="signup"),
    path('login/', views.LoginPage, name='login'),
    path('menu/', views.HomePage, name="menu"),
    path('logout/', views.LogoutPage, name='logout'),
    path('comedor/', views.Comedor, name="comedor"),
    path('novedad/', views.Novedad, name="novedad"),
    path('hambu/', views.Hambu, name="hambu"),
    path('hotdog/', views.Hotdog, name="hotdog"),
    path('flautas/', views.Flautas, name="flautas"),
    path('molletes/', views.Molletes, name="molletes"),
    path('comida/', views.Comida, name="comida"),
    path('chila/', views.Chilaquiles, name="chila"),
    path('torta/', views.Torta, name="torta"),
    path('contacto/', views.Contacto, name="contacto"),
    path('inicio/', views.Inicio, name="inicio"),
    path('registro/', views.Registro, name="registro"),
    path('encuesta/', views.Enc, name="encuesta"),
]