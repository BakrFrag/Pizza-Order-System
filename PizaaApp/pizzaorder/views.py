from django.shortcuts import render
from pizzaorder.models import Order;
from pizzaorder.serializers import *;
from rest_framework import generics;
# Create your views here.
class ListOrderApi(generics.ListAPIView):
    model=Order;
    qs=Order.objects.all();
    serializer_class=ListOrderSerializer;
    permission_class=[];
class CreteOrderApi(generics.CreateAPIView):
    Model=Order;
    serializer_class=CreateOrderSerializer;
    permission_class=[];
class RetriveOrderApi(generics.RetrieveAPIView):
    model=Order;
    qs=Order.objects.all();
    permission_class=[];
    lookup_field='pk';
class UpdateOrderApi(generics.UpdateAPIView):
    model=Order;
    qs=Order.objects.all();
    permission_class=[];
    lookup_field='pk';
class DeleteOrderApi(generics.DestroyAPIView):
    model=Order;
    qs=Order.objects.all();
    permission_class=[];
    lookup_field='pk';

