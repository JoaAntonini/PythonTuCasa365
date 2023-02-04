from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppCoder.forms import SillonFormulario, MesaFormulario, LamparaFormulario, UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#armo login 
def login_request(request):
      
      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid(): 
                  usuario = form.cleaned_data.get('username')
                  contrasenia = form.cleaned_data.get('password')

                  user = authenticate(username= usuario, password=contrasenia)

                  if user is not None:
                        login(request, user)

                        return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                  else:
                        return render(request, "AppCoder/inicio.html", {"mensaje":f"Datos incorrectos"})
      
            else:

                  return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

      form = AuthenticationForm()

      return render(request, "AppCoder/login.html", {"form": form})

# Vista de registro
def register(request):

      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :"})

      else:
            form = UserCreationForm()
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

#solicita login si o si para el inicio


def inicio(request):
      return render(request, "AppCoder/inicio.html")

#Para editar el perfil
@login_required
def editarPerfil(request):
      
      usuario = request.user

      if request.method == 'POST':

            miFormulario = UserEditForm(request.POST)

            if miFormulario.is_valid():

                  informacion = miFormulario.cleaned_data

                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']

                  usuario.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario = UserEditForm(initial={'email': usuario.email})

      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})



def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      
      return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})


# ubicacion HTML
def inicio(request):

      return render(request, "AppCoder/inicio.html")

def sillones(request):   
      
      return render(request, "AppCoder/sillones.html")

def mesas(request):

      return render(request, "AppCoder/mesas.html")


def lamparas(request):

      return render(request, "AppCoder/lamparas.html")


def busqueda(request):

      return render(request, "AppCoder/busquedaModelos.html")

#FORMULARIOS
@login_required
def sillonFormulario(request):
      if request.method == "POST":

            miFormulario = SillonFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  sillon = Sillon(nombre=informacion["sillon"], precio=informacion["precio"], stock=informacion["stock"])
                  sillon.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = SillonFormulario()

      return render(request, "AppCoder/sillonFormulario.html", {"miFormulario": miFormulario})


@login_required
def mesaFormulario(request):
      if request.method == "POST":

            miFormulario = MesaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  mesa = Mesas(nombre=informacion["mesa"], precio=informacion["precio"],color=informacion["color"],stock=informacion["stock"] )
                  mesa.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = MesaFormulario()

      return render(request, "AppCoder/mesaFormulario.html", {"miFormulario": miFormulario})

@login_required
def lamparaFormulario(request):
      if request.method == "POST":

            miFormulario = LamparaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  lampara = Lamparas(nombre=informacion["lampara"], precio=informacion["precio"],tamaño=informacion["tamaño"],stock=informacion["stock"] )
                  lampara.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = LamparaFormulario()
 
      return render(request, "AppCoder/lamparaFormulario.html", {"miFormulario": miFormulario})

##

def busquedaModelos(request):
      return render(request, "AppCoder/busquedaModelos.html")



def buscarSillon(request):
      
      respuesta = f"Estoy buscando el precio del modelo de sillon: {request.GET['sillon']}"
      
      #No olvidar from django.http import HttpResponse
      
      return HttpResponse(respuesta)


def buscarMesa(request):
      
      respuesta = f"Estoy buscando el precio de la mesa: {request.GET['mesa']}"
      
      #No olvidar from django.http import HttpResponse
      
      return HttpResponse(respuesta)

def buscarLampara(request):
      
      respuesta = f"Estoy buscando el precio de la lampara: {request.GET['lampara']}"
      
      #No olvidar from django.http import HttpResponse
      
      return HttpResponse(respuesta)

#muestra el detalle de las lamparas
def leerLamparas(request):
      lamparas = Lamparas.objects.all()
      
      contexto = {"lamparas":lamparas}

      return render(request, "AppCoder/leerLamparas.html", contexto)

@login_required
def eliminarLamparas(request, nombre):

      lamparas= Lamparas.objects.get(nombre=nombre)
      lamparas.delete()

      lamparas = Lamparas.objects.all()
      
      contexto = {"lamparas":lamparas}

      return render(request, "AppCoder/leerLamparas.html", contexto)

@login_required
def editarLampara(request, nombre):
      
      lampara= Lamparas.objects.get(nombre=nombre)

      if request.method == 'POST':

            miFormulario = LamparaFormulario(request.POST) 
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  
                  lampara.lampara = informacion['lampara']
                  lampara.precio = informacion['precio']
                  lampara.tamaño = informacion['tamaño']
                  lampara.stock = informacion['stock']
                  
                  lampara.save()

                  return render(request, "AppCoder/inicio.html")
      
      else:
            miFormulario = LamparaFormulario(initial={'lampara': lampara.nombre, 'precio': lampara.precio,'tamaño': lampara.tamaño, 'stock': lampara.stock})

      return render(request, "AppCoder/editarLampara.html", {"miFormulario": miFormulario, "nombre": nombre})



#####MESAS 
#Creo una clase para ver los modelos de mesa, creo un html mesa_list y url

class MesaList(ListView):
      
      model = Mesas
      template_name = "AppCoder/mesa_list.html"
      

# creo una clase para ver el detalle de cada mesa, creo un html mesa_list y url

class MesaDetalle(DetailView):
      
      model = Mesas
      template_name = "AppCoder/mesa_detalle.html"
      

#creo un nuevo producto 

class MesaCreacion(LoginRequiredMixin,CreateView):
      
      model = Mesas
      success_url = "/AppCoder/mesas/list"
      fields = ['nombre', 'precio', 'color', 'stock']
      
# Modifico datos de un producto

class MesaUpdate(LoginRequiredMixin,UpdateView):
      
      model = Mesas
      success_url = "/AppCoder/mesas/list"
      fields = ['nombre', 'precio', 'color','stock']
      
# Elimino un producto

class MesaDelete(LoginRequiredMixin,DeleteView):
      
      model = Mesas
      success_url = "/AppCoder/mesas/list"


#####LAMPARAS
#Creo una clase para ver los modelos de mesa, creo un html mesa_list y url

class LamparaList(ListView):
      
      model = Lamparas
      template_name = "AppCoder/lampara_list.html"
      

# creo una clase para ver el detalle de cada mesa, creo un html mesa_list y url

class LamparaDetalle(DetailView):
      
      model = Lamparas
      template_name = "AppCoder/lampara_detalle.html"
      

#creo un nuevo producto 

class LamparaCreacion(LoginRequiredMixin,CreateView):
      
      model = Lamparas
      success_url = "/AppCoder/lamparas/list"
      fields = ['nombre', 'precio', 'tamaño', 'stock']
      
# Modifico datos de un producto

class LamparaUpdate(LoginRequiredMixin,UpdateView):
      
      model = Lamparas
      success_url = "/AppCoder/lamparas/list"
      fields = ['nombre', 'precio', 'tamaño', 'stock']
      
      
# Elimino un producto

class LamparaDelete(LoginRequiredMixin,DeleteView):
      
      model = Lamparas
      success_url = "/AppCoder/lamparas/list"


#####SILLONES
#Creo una clase para ver los modelos de mesa, creo un html mesa_list y url

class SillonList(ListView):
      
      model = Sillon
      template_name = "AppCoder/sillon_list.html"
      

# creo una clase para ver el detalle de cada mesa, creo un html mesa_list y url

class SillonDetalle(DetailView):
      
      model = Sillon
      template_name = "AppCoder/sillon_detalle.html"
      

#creo un nuevo producto 

class SillonCreacion(LoginRequiredMixin,CreateView):
      
      model = Sillon
      success_url = "/AppCoder/sillones/list"
      fields = ['nombre', 'precio',  'stock']
      
# Modifico datos de un producto

class SillonUpdate(LoginRequiredMixin, UpdateView):
      
      model = Sillon
      success_url = "/AppCoder/sillones/list"
      fields = ['nombre', 'precio', 'stock']
      
      
# Elimino un producto

class SillonDelete(LoginRequiredMixin, DeleteView):
      
      model = Sillon
      success_url = "/AppCoder/sillones/list"     
      

