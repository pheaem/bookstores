from django.shortcuts import render

# Create your views here.
class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'
    context_object_name = 'author'

class CategoryListView(ListView):
    model = Category
    template_name = 'books/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'books/category_detail.html'
    context_object_name = 'category'

class BookListView(ListView):
    model = Books
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Books
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookImportListView(ListView):
    model = Book_Import
    template_name = 'imports/book_import_list.html'
    context_object_name = 'book_imports'

class BookImportDetailView(DetailView):
    model = Book_Import
    template_name = 'imports/book_import_detail.html'
    context_object_name = 'book_import'

class CartListView(ListView):
    model = Cart
    template_name = 'sales/cart_list.html'
    context_object_name = 'carts'

class CartDetailView(DetailView):
    model = Cart
    template_name = 'sales/cart_detail.html'
    context_object_name = 'cart'

class CheckoutListView(ListView):
    model = Checkout
    template_name = 'sales/checkout_list.html'
    context_object_name = 'checkouts'

class CheckoutDetailView(DetailView):
    model = Checkout
    template_name = 'sales/checkout_detail.html'
    context_object_name = 'checkout'

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'
