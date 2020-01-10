from django.db import models


pizza_size=[("L","Large"),("M","Medium"),("S","Small")]
# this types from internet
pizza_type=[("Sicilian","Sicilian"),("Margherita","Margherita"),
("Greek ","Greek",("Checken","Checken","Chesse","Chesse"))];
order_status=[("Shipped","Shipped Number"),("in_progress","In Prigress"),("canceled","Canceled"),("Delivered","delivered")];
# Create your models here.
class Order(models.Model):
    #Customer Info
    
    customer_name=models.CharField(max_length=256);
    customer_addres=models.CharField(max_length=256);
    customer_phone=models.CharField(max_length=256);
    
    #Pizza Info
    
    pizza_type=models.CharField(max_length=256,choices=pizza_type);
    pizza_size=models.CharField(max_length=256,choices=pizza_size);
    pizza_number=models.IntegerField();
    
    #Order Info
    status=models.CharField(max_length=256,choices=order_status);
    updated=models.DateTimeField(auto_now=True);
    created=models.DateTimeField(auto_now_add=True);
    def __str__(self):
        return f"Order For Customer{self.customer_name} With Pizzaa Type {self.pizza_type}";