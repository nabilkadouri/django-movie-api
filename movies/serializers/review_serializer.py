from rest_framework import serializers
from movies.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["user"]
       
        
    def validate_rating(self, value):
        
        if value <= 0 or value > 10:
            raise serializers.ValidationError(
                "La note doit être comprise entre 1 et 10."
            )
        
        return value
    
    
    def validate_comment(self, value):
        return value.strip() if value else value
    
    
    def validate(self, data):
        
        request = self.context.get("request")
        
        user = request.user
        movie = data.get("movie")
        
        if Review.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError(
                "Le film sélectionné ne doit pas être noté plusieurs fois."
            )
            
        return data
    
    
class ReviewUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = [
            "rating",
            "comment"
        ]
        
    def validate_comment(self, value):
    
        return value.strip()
    
    
    def validate_rating(self, value):
    
        if value <= 0 or value > 10:
            raise serializers.ValidationError(
                "La note doit être comprise entre 1 et 10."
            )
        
        return value
    
    
               
            