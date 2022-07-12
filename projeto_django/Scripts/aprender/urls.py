
from django.contrib import admin
from django.urls import path, re_path
from . import views
from .views import home, classe # usado dentro da pasta #
from clientes.views import cliente #usando em outra pasta fora
from fornecedores.views import fornecedor #usando em outra pasta fora 
# criando caminhos para o site ##
urlpatterns = [
    re_path('$', views.home), # usado em pasta dentro 
    re_path('cliente/$',cliente), #usando em pasta fora
    re_path('fornecedor/$', fornecedor),#usando em pasta fora 
    re_path(r'^classe/(?P<id>\d+)$', views.classe),
    path(r'admin/', admin.site.urls),
]
