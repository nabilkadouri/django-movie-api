from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from movies.serializers import ReviewSerializer, ReviewUpdateSerializer
from movies.models import Review


class ReviewView(APIView):
    
    def post(self, request):
        
        serializer = ReviewSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        
        
        reviews = Review.objects.all()
        
        serializer = ReviewSerializer(
            reviews,
            many=True
        )
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ReviewDetailView(APIView):
    
    def get(self, request, pk=None):
        
        review = get_object_or_404(
            Review,
            pk=pk
        )
        
        serializer = ReviewSerializer(review)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def patch(self, request, pk=None):
        
        review = get_object_or_404(
            Review,
            pk=pk
        )
        
        serializer = ReviewUpdateSerializer(
            review,
            data=request.data,
            partial=True
        )
        
        if serializer.is_valid():
            
            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk=None):
        
        review = get_object_or_404(Review, pk=pk)
        
        review.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    