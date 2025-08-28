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

def pizza(request, pizza_id):
    """The page with ingredients of a pizza"""
    pizza = Pizza.objects.get(id=pizza_id)  # pizza_id is a reference to pizza.id
    toppings = pizza.topping_set.all()   # reverse lookup to collect all ingredients object (Topping QuerySet)
    context = {'pizza_key': pizza, 'toppings_key': toppings}
    return render(request, 'pizzas/pizza.html', context)