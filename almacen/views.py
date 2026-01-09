from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido a la página principal")

def get_date(request):
    date=datetime.now()
    html = f'<h1>fecha actual: {date}</h1>'
    return HttpResponse(html)