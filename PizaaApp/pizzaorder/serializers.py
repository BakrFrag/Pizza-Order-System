from rest_framework import serializers;
class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order;
        fields="__all__";
class RetriveOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order;
        fields="__all__";