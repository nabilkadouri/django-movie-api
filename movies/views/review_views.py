from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from movies.serializers import ReviewSerializer, ReviewUpdateSerializer
from movies.models import Review
from movies.permissions.review_permissions import IsOwnerReview
class ReviewView(APIView):
    
    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
    
    
    def post(self, request):
        
        serializer = ReviewSerializer(
            data=request.data,
            context={"request": request}
        )
        
        if serializer.is_valid():
            
            serializer.save(user=request.user)
            
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
    
    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [
            IsAuthenticated(),
            IsOwnerReview()
        ]
    
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
        
        self.check_object_permissions(
            request,
            review
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
        
        review = get_object_or_404(
            Review,
            pk=pk,
            )
        
        self.check_object_permissions(
            request,
            review
        )
        
        review.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    