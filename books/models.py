from django.core.validators import MinValueValidator, MaxValueValidator	
from django.contrib.auth.models import User
import uuid
from django.db import models

class Author(models.Model):
    author_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.author_name

class Category(models.Model):
    category_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

class Books(models.Model):
    book_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='books')
    language = models.CharField(max_length=100)
    quantity = models.SmallIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    published_date = models.SmallIntegerField(validators=[MinValueValidator(0)])
    import_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return f"{self.title} ({self.author.author_name})"
        # return self.title

    class Meta:
        ordering = ['title']

class Book_Import(models.Model):
    book_import_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    import_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} ({self.book_import_id})"

    @property
    def import_price(self):
        return self.book.import_price

    class Meta:
        ordering = ['book']

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