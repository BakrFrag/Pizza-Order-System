from django.contrib import admin
from django.urls import path,include;

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include Pizzaorder App
    
    path('pizza/',include("pizzaorder.urls"))
];
