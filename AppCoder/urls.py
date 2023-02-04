from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),  #ok
    path('sillones', views.sillones, name="Sillones"), #ok
    path('mesas', views.mesas, name="Mesas"), #OK
    path('lamparas', views.lamparas, name="Lamparas"), #OK
    
    path('sillonFormulario', views.sillonFormulario, name="SillonFormulario"), #PERMITE CREAR UNO NUEVO
    path('mesaFormulario', views.mesaFormulario, name="MesaFormulario"), #PERMITE CREAR UNO NUEVO
    path('lamparaFormulario', views.lamparaFormulario, name="LamparaFormulario"), #PERMITE CREAR UNO NUEVO   
    path('busquedaModelos', views.busquedaModelos, name="BusquedaModelos"),#BUSCAR INFO DE UN MODELO
    
    # busqueda de modelos, todos vinculados al html busqueda modelos
    path('buscarSillon/', views.buscarSillon),
    path('buscarMesa/', views.buscarMesa),
    path('buscarLampara/', views.buscarLampara),
    
    
    path('leerLamparas', views.leerLamparas, name = "LeerLamparas"), #ABM DE LAMPARAS    
    path('eliminarLamparas/<nombre>/', views.eliminarLamparas, name = "EliminarLamparas"), 
    path('editarLampara/<nombre>/', views.editarLampara, name = "EditarLampara"),
    
    # Para ABM MESAS
    path('mesas/list', views.MesaList.as_view(), name='List'), #ok    
    path(r'^nuevo$', views.MesaCreacion.as_view(), name= 'Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.MesaUpdate.as_view(), name= 'Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.MesaDelete.as_view(), name= 'Eliminar'),
    
    
    # Para ABM LAMPARAS
    path('lamparas/list', views.LamparaList.as_view(), name='LamparasList'), #ok    
    path(r'^nuevo$', views.LamparaCreacion.as_view(), name= 'LamparasNuevo'),
    path(r'^editarlampara/(?P<pk>\d+)$', views.LamparaUpdate.as_view(), name= 'LamparasEditar'),
    path(r'^borrarlampara/(?P<pk>\d+)$', views.LamparaDelete.as_view(), name= 'LamparasEliminar'),
    
    
    # Para ABM SILLONES
    path('sillones/list', views.SillonList.as_view(), name='SillonesList'), #ok    
    path(r'^nuevo$', views.SillonCreacion.as_view(), name= 'SillonesNuevo'),
    path(r'^editarsillon/(?P<pk>\d+)$', views.SillonUpdate.as_view(), name= 'SillonesEditar'),
    path(r'^borrarsillon/(?P<pk>\d+)$', views.SillonDelete.as_view(), name= 'SillonesEliminar'),
    
    path('login/', views.login_request, name= 'Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil")
]


