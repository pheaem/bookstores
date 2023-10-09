from django.urls import path
from .views import *

urlpatterns = [
    # path('authors/', AuthorList.as_view(), name='author-list'),
    # path('authors/<str:pk>/', AuthorDetail.as_view(), name='author-detail'),
    # path('categories/', CategoryList.as_view(), name='category-list'),
    # path('categories/<str:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('', BookAPIView.as_view(), name='book-list'),
    # path('books/<str:pk>/', BookDetail.as_view(), name='book-detail'),
    # path('book-imports/', BookImportList.as_view(), name='book-import-list'),
    # path('book-imports/<str:pk>/', BookImportDetail.as_view(), name='book-import-detail'),
    
]