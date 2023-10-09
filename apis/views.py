from django.shortcuts import render
from rest_framework import generics

from books.models import *
from .serializers import *

class BookAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class CustomerAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CheckoutAPIView(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class CartAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer