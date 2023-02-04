from django.contrib import admin


from .models import Sillon, Lamparas, Mesas, Avatar

#importamos el archivo models

# #registramos los modelos

admin.site.register(Sillon)

admin.site.register(Lamparas)

admin.site.register(Mesas)

admin.site.register(Avatar)



