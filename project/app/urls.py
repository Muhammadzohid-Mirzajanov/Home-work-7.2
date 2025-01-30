from django.urls import path
from .views import BookListAPIView  # To‘g‘ri import qilinganligiga ishonch hosil qiling

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookListAPIView.as_view(), name='book-detail'),

]
