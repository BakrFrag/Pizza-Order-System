from rest_framework import serializers;
from pizzaorder.models import Order;
class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order;
        fields="__all__";
class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order;
        exclude=['updated','created']
class RetriveOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order;
        fields="__all__";