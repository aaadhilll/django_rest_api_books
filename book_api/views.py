from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all() # It is big complex data
   # books_python = list(books.values()) # Python data structure
   # return JsonResponse({
    #    'books' : books_python
   # })
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST']) 
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)    
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)  #complex data
    except:
        return Response({
            'Error' : 'Book does not exist'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
          #  print('hitiiing of posting')
          #  print(request.data)
          #  print(serializer)
            return Response(serializer.data, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        book.delete()
     #   return Response({
     #       'delete' : True
     #   })
        return Response(status=status.HTTP_204_NO_CONTENT)


