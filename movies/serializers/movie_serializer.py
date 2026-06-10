from rest_framework import serializers
from django.utils import timezone
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ["created_by"]
        
    def validate_title(self,value):
        
        value = value.strip()
        
        if not value:
            raise serializers.ValidationError(
                "Le titre du film ne peut pas être vide."
            )
        
        value = value.title()
        
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le titre doit contenir au moins 3 caractères."
            )

        queryset = Movie.objects.filter(
            title__iexact=value
        )

        if self.instance:
            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():
            raise serializers.ValidationError(
                "Ce film existe déjà."
            )
            
        return value
              
    def validate_description(self,value):
        
        return value.strip()
    
    def validate_release_year(self, value):
        current_year = timezone.now().year
                
        if value > current_year:
            raise serializers.ValidationError(
                "L'année de réalisation du film ne doit pas être dans le futur."
            )
            
        if value < 1888:
            raise serializers.ValidationError(
                "L'année du film est trop ancienne."
            )

        return value
    
    def validate_duration(self, value):
        
        if value < 40:
            raise serializers.ValidationError(
                "Un film doit durer au moins 40 minutes."
            )
            
        return value
    
class MovieUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = [
            "description",
            "image",
            "categories",
            "is_published"
        ]
            
    def validate_description(self,value):
        
        return value.strip()