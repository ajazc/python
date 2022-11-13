from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    html = open('./templates/inicio.html')
    plantilla = Template(html.read()) #Se carga en memoria nuestro documento

    html.close()
    contexto = Context(); #En esete caso no hay nada ya que no hay parametros, IGUAL
                           #hay que crearlo
    documento = plantilla.render(contexto) #renderizamos la plantilla

    return HttpResponse(documento)
