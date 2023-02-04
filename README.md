Proyecto Tu Casa 365
Queremos brindarte un espacio moderno y accesible para que puedas equipar tu casa a tu gusto. Nuestros servicios incluyen la venta y entrega del producto, también brindamos asesoramiento sobre los materiales, su calidad y las mejores combinaciones para tu estilo.
El proyecto se desarrolló en Python utilizando el framework Django. En el mismo se muestran los distintos productos con sus respectivas características y se realiza el ABM de dichos productos. 
Todos los datos son almacenados en la base de datos. Restricciones: personas no registradas en base de datos, no tienen permisos para realizar el ABM de los productos.
Estructura del proyecto:
Models.py: contiene 4 models, con sus respectivos campos y tipos de datos.
•	Sillón
•	Lámparas
•	Mesas
•	Avatar
Admin.py: se habilitaron los 4 models para poder ser visualizados desde el administrador, y ser editados allí.
Forms.py: 
•	3 formularios para crear categorías de productos (Sillones, Lámparas y Mesas)
•	3 formularios para crear y editar el login de los usuarios.
Urls.py: contiene el camino de acceso a las vistas creadas que permiten el funcionamiento de la página. Las mismas van desde el listado de los productos, el login de los usuarios o el ABM de algún producto.
Views.py: Aparecen todas las vistas que se utilizan en la App, junto con las limitaciones de seguridad para cada una y se define donde se termina mostrando el dato. 
Templates: contiene los archivos HTML, que permiten visualizar en el front todo lo desarrollado por el modelo.
Navegabilidad del proyecto:
1)	Lo primero que veremos es la pagina de inicio que contiene:
a.	En el NavBar los 3 tipos de productos que ofrece la empresa, un buscador de precios y el login del usuario.
b.	En el main un breve resumen de quienes somos y que servicios ofrecemos
c.	Un footer con acceso a cada una de nuestras redes sociales
2)	Navegando en las paginas de Sillones, Mesas y Lámparas veremos:
a.	El catálogo de productos, que lleva al detalle
b.	Ofertas de la semana, lleva al inicio por el momento.
c.	Los materiales con los que trabajamos, lleva al inicio por el momento.
d.	Y combinaciones de productos sugeridas, lleva al inicio por el momento.
3)	Dentro del catálogo de cada producto tenemos el ABM de los mismos. Aquí podremos (solamente si tenemos un usuario):
a.	Editar el producto
b.	Eliminar el producto
c.	Sumar un nuevo producto
4)	En el login del usuario (NavBar a la derecha) tenemos las siguientes opciones:
a.	Editar Perfil
b.	Cerrar sesión
i.	Acá nos redirecciona al inicio para poder loguearnos nuevamente.

Video demostración: https://drive.google.com/drive/folders/1J1gAhzg1pMgDXslzuiRTb0jnVm2MFUEq?usp=sharing
SuperUsuario: c02377 Clave: Coder_1234
Johanna Antonini.


