from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido a la página principal")

def get_date(request):
    date=datetime.now()
    html = f'<h1>fecha actual: {date}</h1>'
    return HttpResponse(html)

def get_json(request):
    data = {
        'id': 1,
        'nombre': 'erik',
        'mail': 'erik@almacen.com',
        'age': 25
    }
    return JsonResponse(data)

def get_html(request):
    return render(request, 'index.html')