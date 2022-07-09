
from django.contrib import admin
from django.urls import path, re_path
from . import views
from .views import home, cliente, classe
# criando caminhos para o site ##
urlpatterns = [
    re_path('$', views.home),
    re_path('cliente/$', views.cliente),
    re_path(r'^classe/(?P<id>\d+)$', views.classe),
    path(r'admin/', admin.site.urls),
]
