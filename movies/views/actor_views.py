from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404

from movies.serializers import ActorSerializer
from movies.models import Actor

class ActorView(APIView):
    
    def get_permissions(self):
        
        if self.request.method == 'GET':
            return [AllowAny()]
        
        else:
            return [IsAdminUser()]
        
    
    def post(self, request):
        
        serializer = ActorSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    
    def get(self, request):
        
        actors = Actor.objects.all()
        
        serializer = ActorSerializer(
            actors,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ActorDetailView(APIView):
    
    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAdminUser()]
    
    
    def get(self,request, pk=None):
        
        actor = get_object_or_404(Actor, pk=pk)
        
        serializer = ActorSerializer(actor)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, pk=None):
        
        actor = get_object_or_404(Actor, pk=pk)
        
        actor.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)