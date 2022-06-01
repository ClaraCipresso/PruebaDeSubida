from django.contrib import admin
from django.urls import path
from Proyecto1.views import probando_template
from Proyecto1.views import saludo
from Proyecto1.views import segunda_vista
from Proyecto1.views import dia_de_hoy
from Proyecto1.views import nombre_persona
from Proyecto1.views import probando_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segundavista/', segunda_vista),
    path('diadehoy/', dia_de_hoy),
    path('nombre_persona/<nombre>/', nombre_persona),
    path('probando_template/',probando_template),
]

