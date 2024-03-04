from django.shortcuts import render, redirect # Importamos aqui a função para redirecionar o usuário para outra URL
from django.http import HttpResponse # Essa função retorna a resposta em formato HTTP
from .models import BancoDados # Importa o banco de dados criado, para poder manipulá-lo


# Create your views here.

def funcao_formulario(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'formulario.html', {'statusURL':status})
    
    elif request.method == "POST":
        nome_form = request.POST.get('nome')
        idade_form = request.POST.get('idade')

        pessoa = BancoDados(
            nome=nome_form,
            idade=idade_form
        )
        pessoa.save()

        return redirect('/sistema/formulario/?status=1')
        #return redirect('/url_teste/formulario/')
        #return HttpResponse("Essa pessoa foi salva em sistema.")
    
def listar_pessoas(request):

    nome_filt = request.GET.get('nome_filtrar')
    idade_filt = request.GET.get('idade_filtrar')

    # Em primeira instância, ele recebe todas as informações
    pessoas = BancoDados.objects.all()
    print(pessoas)
    # Se tiver um nome no filtro, ele busca uma pessoa que contém o nome digitado
    if nome_filt:
        pessoas = BancoDados.objects.filter(nome__contains=nome_filt)

    # Se tiver uma idade no filtro, ele busca uma pessoa com aquela idade específica
    if idade_filt:
        # __gte = maior ou igual | __lte = menor ou igual | __gt = maior que | __lt = menor que
        pessoas = BancoDados.objects.filter(idade=idade_filt)        # Idade = Filtro
        #pessoas = BancoDados.objects.filter(idade__gte=idade_filt)  # Idade >= Filtro
        #pessoas = BancoDados.objects.filter(idade__lte=idade_filt)  # Idade <= Filtro
        #pessoas = BancoDados.objects.filter(idade__gt=idade_filt)   # Idade > Filtro
        #pessoas = BancoDados.objects.filter(idade__lt=idade_filt)   # Idade < Filtro

    return render(request, "lista_pessoas.html", {'pessoas':pessoas})

def ver_pessoas(request, id_pessoa):
    pessoa = BancoDados.objects.get(id=id_pessoa)
    return render(request, 'pessoa.html', {'pessoa':pessoa})

def deletar_pessoas(request, id_pessoa):
    pessoa = BancoDados.objects.get(id=id_pessoa)
    # O comando delete() já deleta a pessoa do banco
    pessoa.delete()
    return redirect('/sistema/pessoas/')