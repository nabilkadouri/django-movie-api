from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from movies.serializers import FavoriteSerializer
from movies.models import Favorite
from movies.permissions.favorite_permissions import IsOwnerFavorite

class FavoriteView(APIView):

    def get_permissions(self):

        if self.request.method in ["GET", "POST"]:
            return [IsAuthenticated()]

        elif self.request.method == "DELETE":
            return [
                IsAuthenticated(),
                IsOwnerFavorite()
            ]

        return super().get_permissions()
    
    
    def post(self, request):
        
        serializer = FavoriteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        
        favorites = Favorite.objects.filter(user=request.user)
        
        serializer = FavoriteSerializer(
            favorites,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, pk=None):
        
        favorite = get_object_or_404(
            Favorite,
            pk=pk,
            )
        
        self.check_object_permissions(
            request,
            favorite
        )
            
        favorite.delete()
        
        return Response(
            status=status.HTTP_204_NO_CONTENT
            )
        
        