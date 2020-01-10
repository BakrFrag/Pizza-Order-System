from django.test import TestCase;
from django.urls import reverse;
from rest_framework.test import APIClient
# Create your tests here.
from .models import Order;
# test list order views Get Repuest

class TestListOrderApi(TestCase):
    def test_List(self):
        client=APIClient();
        response=client.get(reverse("pizza_orders"),format='json');
        self.assertEqual(response.status_code,200);

# test create order Post Request

class TestCreateOrderApi(TestCase):
    def test_create(self):
        client=APIClient();
        response=client.post(reverse('create_order'),{"customer_name":"Bk Test","customer_address":"Menofia","customer_phone":"01092276430"});
        self.assertEqual(response.status_code,400);

#test delete item not exist Delete Request

class TestDestoryOrderApi(TestCase):
    def test_delete(self):
        client=APIClient();
        response=client.delete(reverse("delete_order",
        kwargs={"pk":5000}));
        self.assertEqual(response.status_code,404);

