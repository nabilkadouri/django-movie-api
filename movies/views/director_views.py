from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from movies.serializers import DirectorSerializer

class DirectorView(APIView):
    
    def post(self, request):
        
        serializer = DirectorSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            result = serializer.data
            
            return Response(result, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)