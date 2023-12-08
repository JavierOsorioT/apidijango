# En tu archivo tests.py dentro de la aplicación

#import pytest
#from django.utils import timezone
#from .models import Respuestaschatbot, Registros

#@pytest.fixture
#def respuesta_chatbot():
 #   return Respuestaschatbot.objects.create(
  #      marca_temporal=timezone.now(),
   #     nombre_completo="Usuario de Prueba",
    #    pregunta1="A",
     #   pregunta2="Esta es una pregunta de prueba",
      #  pregunta3="1234567890",
       # pregunta4="Otra pregunta de prueba",
        #pregunta5="Otra pregunta más",
        #pregunta6="Alguna respuesta",
        #pregunta7="Respuesta corta"
    #)

#@pytest.fixture
#def registro_usuario():
#    return Registros.objects.create(
#        user="nombredeusuario",
#        password="contraseña",
#        password_repeat="contraseña",
#        email="correo@example.com"
#    )

#def test_respuesta_chatbot_str(respuesta_chatbot):
#    assert str(respuesta_chatbot) == "Usuario de Prueba"
#
#def test_registro_usuario_campos(registro_usuario):
#    assert registro_usuario.user == "nombredeusuario"
#    assert registro_usuario.password == "contraseña"
#    assert registro_usuario.password_repeat == "contraseña"
#    assert registro_usuario.email == "correo@example.com"
#