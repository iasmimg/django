"""
URL configuration for site01 project.

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
from core.views import inicial, contato,seila #está importando porque está em pastas diferentes


urlpatterns = [
    path('admin/', admin.site.urls),
    #criando uma nova rota
    path('',inicial, name='inicial'),
    path('contato/',contato, name='contato'),
    path('seila/',seila)
]
