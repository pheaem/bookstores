from django.urls import path
from .views import *

urlpatterns = [
    # path('authors/', AuthorList.as_view(), name='author-list'),
    # path('authors/<str:pk>/', AuthorDetail.as_view(), name='author-detail'),
    # path('categories/', CategoryList.as_view(), name='category-list'),
    # path('categories/<str:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('books/', BookAPIView.as_view(), name='book-list'),
    path('books/<str:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('customers/', CustomerAPIView.as_view(), name='customer-list'),

]