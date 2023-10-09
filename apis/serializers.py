from rest_framework import serializers

from books.models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'author', 'publisher', 'category', 'language', 'quantity', 'description', 'published_date', 'sale_price', 'discount', 'status', 'cover')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_name', 'status')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', 'status')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('book', 'quantity')

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ('customer', 'book', 'quantity', 'total')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_name', 'customer_phone', 'customer_address')
    
    # def create(self, validated_data):
    #     customer_data = Customer.objects.create(**validated_data)
    #     return customer_data