from rest_framework import serializers
from movies.models import Favorite
from django.contrib.auth.models import User



class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favorite
        fields = "__all__"
        
    def validate(self, data):
        user = data.get("user")
        movie = data.get("movie")
        
        if Favorite.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError(
                "Le film sélectionné a déjà été mis en favori."
            )
            
        return data