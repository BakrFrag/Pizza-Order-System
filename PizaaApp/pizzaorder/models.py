from django.db import models


pizza_sizes=(
    ("l","Large"),
    ("m","Medium"),
    ("s","Small")
    );
# this types from internet
pizza_types=(
    ("sicilian","Sicilian"),
    ("margherita","Margherita"),
    ("greek","Greek"),
    ("checken","Checken"),
    ("chesse","Chesse"));
order_status=(
    ("shipped","Shipped Number"),
    ("in_progress","In Prigress"),
    ("canceled","Canceled"),
    ("Delivered","delivered")
        );
# Create your models here.
class Order(models.Model):
    #Customer Info
    
    customer_name=models.CharField(max_length=256);
    customer_addres=models.CharField(max_length=256);
    customer_phone=models.CharField(max_length=256);
    
    #Pizza Info
    
    pizza_type=models.CharField(max_length=256,
    default="chesse",choices=pizza_types);
    pizza_size=models.CharField(max_length=256,default="m",choices=pizza_sizes);
    pizza_number=models.PositiveIntegerField(default=1,
    validators=[MinValueValidator(1), MaxValueValidator(100)]);
    
    #Order Info
    status=models.CharField(max_length=256,default="shipped",choices=order_status);
    updated=models.DateTimeField(auto_now=True);
    created=models.DateTimeField(auto_now_add=True);
    def __str__(self):
        return f"Order For Customer{self.customer_name} With Pizzaa Type {self.pizza_type}";