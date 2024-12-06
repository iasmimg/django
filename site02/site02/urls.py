"""
URL configuration for site02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import nome, cadastro, soma, subtracao, multiplicacao, divisao


urlpatterns = [
    path('nome/', nome, name='nome'),
    path('cadastro/<str:nome>/<int:idade>/<str:curso>/', cadastro, name='cadastro'),
    path('soma/<int:numero_1>/<int:numero_2>/', soma, name='soma'),
    path('subtracao/<int:numero_1>/<int:numero_2>/', subtracao, name='subtracao'),
    path('multiplicacao/<int:numero_1>/<int:numero_2>/', multiplicacao, name='multiplicacao'),
    path('divisao/<int:numero_1>/<int:numero_2>/', divisao, name='divisao'),
    path('admin/', admin.site.urls),
]
