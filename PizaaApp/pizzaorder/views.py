from django.shortcuts import render
from pizzaorder.models import Order;
from pizzaorder.serializers import *;
from rest_framework import generics;
from rest_framework.exceptions import APIException;
# Create your views here.

# list all orders GET REQUEST
class ListOrderApi(generics.ListAPIView):
    model=Order;
    #queryset=Order.objects.all();
    serializer_class=RetriveOrderSerializer
    permission_classes=[];

    # allow filter via customer name or status or both of them 
    #  
    def get_queryset(self):
        filter_status=self.request.GET.get('status',None);
        filter_customer=self.request.GET.get('customer',None);
        if filter_status is not None and filter_customer is not None:
            queryset=Order.objects.filter(status__icontains=filter_status,customer_name__icontains=filter_customer).order_by("-created");
            return queryset;
        elif filter_status is not None:
            queryset=Order.objects.filter(status__icontains=filter_status).order_by("-created");
            return queryset;
        elif filter_customer is not None:
            queryset=Order.objects.filter(customer_name__icontains=filter_customer).order_by('-created');
            return queryset;
        else:
            queryset=Order.objects.all().order_by("-created");
            return queryset;

# create order with POST REQUEST
class CreteOrderApi(generics.CreateAPIView):
    Model=Order;
    serializer_class=CreateOrderSerializer;
    permission_class=[];

# Retrieve Single Object GET REQUEST
class RetriveOrderApi(generics.RetrieveAPIView):
    model=Order;
    queryset=Order.objects.all();
    serializer_class=RetriveOrderSerializer
    permission_class=[];
    lookup_field='pk';

# Update Order PUT REQUEST
class UpdateOrderApi(generics.RetrieveUpdateAPIView):
    model=Order;
    queryset=Order.objects.all();
    serializer_class=CreateOrderSerializer
    permission_class=[];
    lookup_field='pk';

    # Custimize Put Request 

    def put(self,request,*args,**kwargs):
        obj=self.get_object();
        if obj.status in ["canceled","delivered"]:
            raise APIException("Canceled order Or Delivered Order Can't Be Updated");
        return self.update(request,*args,**kwargs);

# Remove Order Delete Request
class DeleteOrderApi(generics.RetrieveDestroyAPIView):
    model=Order;
    queryset=Order.objects.all();
    permission_class=[];
    lookup_field='pk';
    serializer_class=RetriveOrderSerializer

