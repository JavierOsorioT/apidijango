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
from api import views
#from . import views  # Importa todas las vistas de tu aplicación actual

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', Home.as_view(), name='index'),
    # path('registro.html', Registro.as_view(), name='registro'),
    # path('recuperar.html', Recuperar.as_view(), name='recuperar'),
    # path('menu.html', Menu.as_view(), name='menu'),
    # path('registrarUser/', Home.registrarUser, name='registrarUser'),
    # path('menucomida.html', Menucomida.as_view(), name='menucomida'),
    #('menucomida.html', index.as_view(), name='index'),
    
    path('', views.SignupPage, name="signup"),
    #path('registrarUsuario/', views.registrarUsuario),
    path('login/', views.LoginPage, name='login'),
    path('menu/', views.HomePage, name="menu"),
    path('logout/', views.LogoutPage, name='logout'),
    path('comedor/', views.Comedor, name="comedor"),
    path('encuesta/', views.Enc, name="encuesta"),
   # path('encuestaxd/', views.Enc2, name="encuestaxd"),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
