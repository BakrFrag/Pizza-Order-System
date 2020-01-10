from django.test import TestCase, Client;
from django.urls import reverse;
# Create your tests here.
from pizzaorder import Order;
class TestListApi(TestCase):
    def setup(self):
        self.client=Client();
        self.response=client.get(reverse("pizza_orders"));
    def Test_List(self):
        self.assertEqual(response.status_code,200);

