from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from movies.serializers import MovieSerializer
from movies.models import Movie

class MovieView(APIView):
    
    def post(self, request):
        
        serializer = MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            result = serializer.data
            
            return Response(result,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        
        movies = Movie.objects.all()
        
        serializer = MovieSerializer(
            movies,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
class MovieDetailView(APIView):
    
    def get(self, request, pk=None):
        
        movie = get_object_or_404(Movie, pk=pk)
        
        serializer = MovieSerializer(movie)
        
        return Response(serializer.data, status=status.HTTP_200_OK)