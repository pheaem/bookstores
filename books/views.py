from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse
from .models import Books, Author, Category, Book_Import

# Author
class AuthorListView(ListView):
    model = Author
    template_name = 'books/authors/author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.filter(status=True)

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'books/authors/author_edit.html'
    fields = '__all__'

    def get_form(self):
        form = super().get_form()
        form.fields['author_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['status'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        return form

    def get_success_url(self):
        return reverse('author-list')

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'books/authors/author_edit.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('author-list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'books/authors/author_delete.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('author-list')

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/authors/author_detail.html'
    context_object_name = 'author'

# Category

class CategoryListView(ListView):
    model = Category
    template_name = 'books/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(status=True)

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'books/category_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'books/category_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'books/category_delete.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('category-list') 


# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = 'books/category_detail.html'
#     context_object_name = 'category'

# class BookListView(ListView):
#     model = Books
#     template_name = 'books/book_list.html'
#     context_object_name = 'books'

# class BookDetailView(DetailView):
#     model = Books
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

# class BookImportListView(ListView):
#     model = Book_Import
#     template_name = 'imports/book_import_list.html'
#     context_object_name = 'book_imports'

# class BookImportDetailView(DetailView):
#     model = Book_Import
#     template_name = 'imports/book_import_detail.html'
#     context_object_name = 'book_import'


