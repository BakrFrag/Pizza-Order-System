from django.contrib import admin
from django.urls import path;
from pizzaorder import views;

urlpatterns = [
    path("list/api/",views.ListOrderApi.as_view(),name="pizza_orders"),
    path("order/<int:pk>/",views.RetriveOrderApi.as_view(),name="view_order"),
    path("create/api/",views.CreteOrderApi.as_view(),name="create_order"),
    path("update/api/<int:pk>/",views.UpdateOrderApi.as_view(),name="update_order"),
    path("delete/api/<int:pk>/",views.DeleteOrderApi.as_view(),name="delete_order"),
]
