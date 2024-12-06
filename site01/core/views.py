from django.shortcuts import render

# Create your views here.
#criando uma função chamada inicial
#está vindo de uma rota por causa do request
def inicial(request):
    return render(request, "index.html")

def contato(request):
    return render(request, "contato.html")

def seila(request):
    return render(request, "seila.html")
