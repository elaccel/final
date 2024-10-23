
from django.contrib import admin
from django.urls import path
from loja import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.lista_produtos, name='lista_produtos'),
]
