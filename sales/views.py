from django.shortcuts import render

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