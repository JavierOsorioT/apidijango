#from rest_framework.views import APIView
from django.shortcuts import render, redirect
#from .models import Registros
from django.contrib import messages
#Mensaje para email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Respuestaschatbot
from django.db.models import Sum

from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='login')

#PAra la graficas
def grafica(request):
    registros = Respuestaschatbot.objects.all()
    return {'registros': registros}

def consulta1(request):
    # Realiza una consulta que cuente las filas con 'SI' en la columna pregunta1
    count = Respuestaschatbot.objects.filter(pregunta1="Si").count()
    return {'count_si': count}

def consulta2(request):
    # Realiza una consulta que cuente las filas con 'NO' en la columna pregunta1
    count2 = Respuestaschatbot.objects.filter(pregunta1="No").count()
    return {'count_no': count2}

def HomePage(request):
    grafica_data = grafica(request)
    tuvista_data = consulta1(request)
    tuvista_data2 = consulta2(request)
    
    # Combina los contextos de ambas vistas en un solo diccionario
    context = {**grafica_data, **tuvista_data, **tuvista_data2}
    return render(request, 'menu.html', context)

def Enc(request):
    
    grafica_data = grafica(request)
    tuvista_data = consulta1(request)
    tuvista_data2 = consulta2(request)
    
    # Combina los contextos de ambas vistas en un solo diccionario
    context = {**grafica_data, **tuvista_data, **tuvista_data2}
    return render (request, 'encuesta.html',context)
################################################################################

#Registro de usuarios
def SignupPage(request):
    """b"""
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        #pass2=request.POST.get('password2')
        
        if pass1!=pass1:
            return ("La Contraseña no coincide")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            
            contact(request)
            
            return redirect('login')
        
    return render (request,'index.html')

def LoginPage(request):
    """c"""
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('menu')
        else:
            return HttpResponse ("El Usuario o Contraseña son Incorrectos")
    return render (request, 'index.html')

########################################################Paginas############################################################################### 
def LogoutPage(request):
    logout(request)
    return redirect('login')
                            
def Comedor(request):
    return render (request, 'menucomida.html')

def Inicio(request):
    return render (request, 'inicio.html')

def Registro(request):
    return render (request, 'registro.html')
def Novedad(request):
    return render (request, 'novedad.html')

#######################################################Correo################################################################################     
def contact(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        #subject=request.POST['subject']
        #message=request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': username,
            'email': email,
            #'message': message
        })
        
        email = EmailMessage(
            subject='Confirmacion de registro',
            body=template,
            from_email=settings.EMAIL_HOST_USER,
            to=[email]
                            )
        
        email.fail_silenty = False
        email.send()
        messages.success(request, "Se ha enviado tu correo")
        return redirect('login')
        
# class Home (APIView):
#     template_name='index.html'
#     def get(self, request):
#         registros = Registros.objects.all()
#         return render(request, self.template_name, {"index": registros})
#     @staticmethod
#     def registrarUser(request):
#         Nombre = request.POST.get('user_name')
#         Correo = request.POST.get('user_email')
#         Contraseña = request.POST.get('user_pass')
        
#         Registros = Registros.objets.create(Nombre=Nombre, Correo=Correo, Contraseña=Contraseña)
#         return redirect ('/')
# class Registro(APIView):
#     template_name='registro.html'
#     def get (self,request):
#         return render(request,self.template_name)
    
# class Recuperar(APIView):
#     template_name='recuperar.html'
#     def get (self,request):
#         return render(request,self.template_name)
    
# class Menu(APIView):
#     template_name='menu.html'
#     def get (self,request):
#         return render(request,self.template_name)
    
# class Menucomida(APIView):
#     template_name='menucomida.html'
#     def get (self,request):
#         return render(request,self.template_name)
    