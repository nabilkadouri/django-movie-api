from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404

from movies.serializers import CategorySerializer
from movies.models import Category

class CategoryView(APIView):
    
    def get_permissions(self):
        
        if self.request.method == 'GET':
            return [AllowAny()]
        
        else:
            return [IsAdminUser()]
        
    
    def post(self, request):
    
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        
        categories = Category.objects.all()
        
        serializer = CategorySerializer(
            categories,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def patch(self, request, pk=None):

        category = get_object_or_404(Category, pk=pk)
        
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk=None):
        
        category = get_object_or_404(Category, pk=pk)
        
        category.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)