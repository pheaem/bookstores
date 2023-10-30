from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from books.models import *
from .serializers import *

class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'genre', 'language']

class BookDetailAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    lookup_field = 'pk'

class CustomerAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'pk'

class CheckoutAPIView(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def post(self, request, *args, **kwargs):
        book_pk = request.data.get('book_id')
        customer_pk = request.data.get('customer_id')

        book = get_object_or_404(Books, pk=book_pk)
        customer = get_object_or_404(Customer, pk=customer_pk)

        checkout = Checkout.objects.create(book=book, customer=customer)

        serializer = CheckoutSerializer(checkout)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer