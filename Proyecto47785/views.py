from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - AL FIIIINN ;O")
def saludo_html(request):
   return HttpResponse("<b>Hola Django</b> - AL FIIIINN ;O")
def saludo_nombre(request, nombre):
   return HttpResponse(f"<h1>{nombre}</h1><br><b>Hola Django</b> - AL FIIIINN ;O")

def saludo_plantilla(request):
    contexto = {
        "nombre": "Jose",
        "edad": 34,
        "pais": "Costa Rica",
        "ciudad": "San José",
        "hijos": [
            {"nombre": "hijo1",
            "edad": 34},
            {"nombre": "hijo2",
             "edad": 24}
        ],
    }
    return render(request,"index.html",contexto)