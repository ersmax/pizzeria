from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Defining a new pizza that can be ordered"""
    name = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return the name of the pizza"""
        return self.name
    
class Topping(models.Model):
    """Defining a topping that can be added to Pizza"""
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return the name of the toppings"""
        if len(self.name) < 50:
            return self.name
        return f"{self.name[:50]}..."


