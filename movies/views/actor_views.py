from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from movies.serializers import ActorSerializer
from movies.models import Actor

class ActorView(APIView):
    
    def post(self, request):
        
        serializer = ActorSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    def get(self, request):
        
        actors = Actor.objects.all()
        
        serializer = ActorSerializer(
            actors,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ActorDetailView(APIView):
    
    def get(self,request, pk=None):
        
        actor = get_object_or_404(Actor, pk=pk)
        
        serializer = ActorSerializer(actor)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, pk=None):
        
        actor = get_object_or_404(Actor, pk=pk)
        
        actor.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)