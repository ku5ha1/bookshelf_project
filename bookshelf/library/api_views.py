from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer, CategorySerializer
from .models import Book, Category
from django.http import Http404

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ToggleReadStatus(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        
    def put(self, request, pk):
        book = self.get_object(pk)
        book.is_read = not book.is_read
        book.save()

        serializer = BookSerializer(book)
        return Response(serializer.data)


class CategoryView(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404


    def get(self, request, format=None):
        categories = Category.objects.all()
        if not categories:
            raise Http404
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(data="Category deleted", status=status.HTTP_204_NO_CONTENT)