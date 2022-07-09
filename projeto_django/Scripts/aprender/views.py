from django.http import HttpResponse 


def home(request):
    html = "Hello word"
    return HttpResponse(html)

def cliente(request):
    html = "Pagina de cliente"
    return HttpResponse(html)

def classe(request, id): 
    var = " Pagina de classes "
    return HttpResponse(var)

