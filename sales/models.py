from django.db import models
import uuid
from books.models import Books

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.book

    class Meta:
        ordering = ['book']

class Customer(models.Model):
    customer_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    customer_address = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name

    class Meta:
        ordering = ['customer_name']

class Checkout(models.Model):
    checkout_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # customer_name = models.CharField(max_length=100)
    # customer_phone = models.CharField(max_length=100)
    # customer_address = models.TextField()
    customer_detail = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.checkout_id
    
    class Meta:
        ordering = ['checkout_id']

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id

    class Meta:
        ordering = ['transaction_id']

class Sale_Report(models.Model):
    sale_report_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.sale_report_id

    class Meta:
        ordering = ['sale_report_id']