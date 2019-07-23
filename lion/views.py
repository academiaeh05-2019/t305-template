from django.shortcuts import render

# Create your views here.
def pagina_inicial(request):
    context = {
        "nome": "joao",
        "cachorros":
        ["mel", "tobias", "cacau", "bob", "madona", "radija"]
    }
    return render(request, 'index.html', context)