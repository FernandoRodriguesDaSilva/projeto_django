from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def cliente(request):
    html = "Pagina de cliente na pasta de  App cliente"
    return HttpResponse(html)