from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from movies.serializers import FavoriteSerializer
from movies.models import Favorite

class FavoriteView(APIView):
    
    def post(self, request):
        
        serializer = FavoriteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        
        favorites = Favorite.objects.all()
        
        serializer = FavoriteSerializer(
            favorites,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, pk=None):
        
        favorite = get_object_or_404(Favorite, pk=pk)
        
        favorite.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)