from django.shortcuts import render
from delivery.models import Order
# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.views import View
from rest_framework.decorators import api_view
from requests import request as r
from random import choice

class IndexView(View):
    def get(self, request):
        template = "form.html"
        return render(request, template)

class OrderView(View):
    def get(self, request):
        template = "orders.html"
        r(url="https://google.com", params=[], method="GET")
        orders = Order.objects.all()
        for order in orders:
            order.status = choice(['In progress', "Started", "Completed"])
        return render(request, template, context={"orders": orders})

@api_view(["POST"])
def MakeOrderView(request):
    if request.method == "POST":
        data = request.data
        Order.objects.create(number=data['number'], type=data['type'], weight=data['weight'], shipment_date=data['date_of_shipment'], shipping_date=data['date_of_shipping'])
        return Response(
                status=status.HTTP_201_CREATED
            )



