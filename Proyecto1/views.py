from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import datetime


def saludo(request):
    return HttpResponse('Hola mundo')

def segunda_vista(request):
    return HttpResponse("Segunda vista")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    texto = 'Hoy es: {}'.format(dia)
    return HttpResponse(texto)

def nombre_persona(self, nombre):
    resultado = 'Mi nombre es: <br> <br> {}'. format(nombre)
    return HttpResponse(resultado)

def probando_template(self):

    nombre = 'Bruno'
    apellido = 'Arias'

    lista_de_notas = [2,5,7,6]

    diccionario = {'nombre':nombre, 'apellido':apellido, 'lista_de_notas':lista_de_notas}

    # miHtml = open(r'template1.html')
    # plantilla = Template(miHtml.read())
    # miHtml.close()

    # mi_contexto = Context(diccionario)
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)