from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"
        
    def validate_rating(self, value):
        
        if value <= 0 or value > 10:
            raise serializers.ValidationError(
                "La note doit être comprise entre 1 et 10."
            )
        
        return value
    
    def validate_comment(self, value):
        
        return value.strip()
    
    def validate(self, data):
        
        user = data.get("user")
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
    
    
               
            