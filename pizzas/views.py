from django.shortcuts import render
from .models import Pizza   # import model Pizza for the data to pass to template
# Create your views here.

def index(request):
    """The home page for pizzas app"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """The page Menu with all pizzas"""
    pizzas = Pizza.objects.all()        # QuerySet of all pizzas
    context = {'pizzas_key': pizzas}
    return render(request, 'pizzas/pizzas.html', context)