from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser

from movies.serializers import DirectorSerializer
from movies.models import Director

class DirectorView(APIView):
    
    def get_permissions(self):
        
        if self.request.method == 'GET':
            return [AllowAny()]
        
        else:
            return [IsAdminUser()]
        
    
    def post(self, request):
        
        serializer = DirectorSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            result = serializer.data
            
            return Response(result, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        
        directors = Director.objects.all()
        
        serializer = DirectorSerializer(
            directors,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class DirectorDetailView(APIView):
    
    def get_permissions(self):
        
        if self.request.method == 'GET':
            return [AllowAny()]
        
        else:
            return [IsAdminUser()]
        
    
    def get(self, request, pk=None):
        
        director =get_object_or_404(Director, pk=pk)

        serializer = DirectorSerializer(director)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, pk=None):
        
        director = get_object_or_404(Director, pk=pk)
        
        director.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)