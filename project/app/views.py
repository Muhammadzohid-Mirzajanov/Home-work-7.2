from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status

from django.forms import model_to_dict

from .serializers import BookSerializer
from .models import Book,Janr

class BookListAPIView(APIView):
    queryset = Book.objects.all()

    def get(self, request: Request, pk=None):
        if pk is None:
            books = Book.objects.all()
            return Response(BookSerializer(books, many=True).data)
        else:
            try:
                book = Book.objects.get(pk=pk)
                return Response(BookSerializer(book).data)
            except Book.DoesNotExist:
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request: Request, pk=None):
        if pk:
            return Response("Method POST not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)

    
    def put(self, request: Request, pk=None):
        if not pk:
            return Response("Method PUT not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)  # `data=request.data` qilib berish kerak
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(BookSerializer(book).data)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request: Request, pk=None):
        if not pk:
            return Response("Method DELETE not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
