from django.shortcuts import render
from pizzaorder.models import Order;
from pizzaorder.serializers import *;
from rest_framework import generics;
from rest_framework.exceptions import APIException;
# Create your views here.
class ListOrderApi(generics.ListAPIView):
    model=Order;
    queryset=Order.objects.all();
    serializer_class=RetriveOrderSerializer
    permission_class=[];
class CreteOrderApi(generics.CreateAPIView):
    Model=Order;
    serializer_class=CreateOrderSerializer;
    permission_class=[];
class RetriveOrderApi(generics.RetrieveAPIView):
    model=Order;
    queryset=Order.objects.all();
    serializer_class=RetriveOrderSerializer
    permission_class=[];
    lookup_field='pk';
class UpdateOrderApi(generics.RetrieveUpdateAPIView):
    model=Order;
    queryset=Order.objects.all();
    serializer_class=CreateOrderSerializer
    permission_class=[];
    lookup_field='pk';
    def put(self,request,*args,**kwargs):
        obj=self.get_object();
        if obj.status in ["canceled","delivered"]:
            raise APIException("Canceled order Or Delivered Order Can't Be Updated");
        return self.update(request,*args,**kwargs);
class DeleteOrderApi(generics.RetrieveDestroyAPIView):
    model=Order;
    queryset=Order.objects.all();
    permission_class=[];
    lookup_field='pk';
    serializer_class=RetriveOrderSerializer

