from django.shortcuts import render

# Create your views here.
#criou uma função e joga para quem fez a requisição
def nome(request):
    context = {
        "meu_nome":"Iasmim",
        "idade": 18,
        "curso": "TSI"
    }

    return render(request, 'nome.html', context)

def cadastro(request, nome, idade, curso):
    context = {
        "nome_url": nome,
        "idade_url": idade,
        "curso_url": curso,
    }
    return render(request, 'cadastro.html', context)


    
def soma(request, numero_1, numero_2):
    context = {
        "numero_1": numero_1,
        "numero_2": numero_2,
        "resultado": numero_1 + numero_2,
    }
    return render(request, 'soma.html', context)

def subtracao(request, numero_1, numero_2):
    context = {
        "numero_1": numero_1,
        "numero_2": numero_2,
        "resultado": numero_1 - numero_2,
    }
    return render(request, 'subtracao.html', context)

def multiplicacao(request, numero_1, numero_2):
    context = {
        "numero_1": numero_1,
        "numero_2": numero_2,
        "resultado": numero_1 * numero_2,
    }
    return render(request, 'multiplicacao.html', context)

def divisao(request, numero_1, numero_2):
    context = {
        "numero_1": numero_1,
        "numero_2": numero_2,
        "resultado": numero_1 / numero_2,
    }
    return render(request, 'divisao.html', context)
