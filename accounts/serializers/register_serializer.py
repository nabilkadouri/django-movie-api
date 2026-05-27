from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(
        write_only=True
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate_email(self, value):
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "L'email existe déjà."
            )
            
        return value
    
    def validate(self, data):
        
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        
        if password != confirm_password:
            raise serializers.ValidationError(
                "Le mot de passe de confirmation n'est pas identique au mot de passe."
            )
            
        return data