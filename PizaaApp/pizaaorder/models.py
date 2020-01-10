from django.db import models

# Create your models here.
class Order(models.Model):
    #Customer Info
    
    customer_name=models.CharField(max_length=256);
    customer_addres=models.CharField(max_length=256);
    customer_phone=models.CharField(max_length=256);
    
    #Pizza Info
    
    pizza_type=models.CharField(max_length=256,choices=types);
    pizza_size=models.CharField(max_length=256,choices=sizes);
    pizza_number=models.IntegerField();
    
    #Order Info
    status=models.CharField(max_length=256,choices=order_status);
    updated=models.DateTimeField(auto_now=True);
    created=models.DateTimeField(auto_now_add=True);
    def __str__(self):
        return f"Order For Customer{self.customer_name} With Pizzaa Type {self.pizza_type}";