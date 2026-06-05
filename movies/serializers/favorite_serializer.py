from rest_framework import serializers
from movies.models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ["user"]
        
    def validate(self, data):
        
        request = self.context.get("request")
        
        user = request.user
        movie = data.get("movie")
        
        if Favorite.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError(
                "Le film sélectionné a déjà été mis en favori."
            )
            
        return data