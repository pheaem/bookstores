from django.urls import path
from .views import *

urlpatterns = [
    path('books/author/', AuthorListView.as_view(), name='author-list'),
    path('books/author/<pk>', AuthorDetailView.as_view(), name='author-detail'),

]