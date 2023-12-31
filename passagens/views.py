from django.shortcuts import render
from passagens.forms import PassagemForms


# Create your views here.
def index(request):
    form = PassagemForms()
    contexto = {"form": form}
    return render(request, "passagens/index.html", contexto)


def revisao_consulta(request):
    if request.method == "POST":
        form = PassagemForms(request.POST)
    contexto = {"form": form}
    return render(request, "passagens/minha_consulta.html", contexto)
