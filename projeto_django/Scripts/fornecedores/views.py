from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def fornecedor(request):
    html = "Pagina de fornecedores na pasta de  App fornecedores"
    return HttpResponse(html)