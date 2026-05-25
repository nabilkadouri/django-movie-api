from rest_framework import serializers

from movies.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

    def validate_name(self, value):

        # Nettoyage espaces
        value = value.strip()

        # Vérifie vide
        if not value:
            raise serializers.ValidationError(
                "Le nom de la catégorie ne peut pas être vide."
            )

        # Format propre
        value = value.title()

        # Taille minimale
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le nom doit contenir au moins 3 caractères."
            )

        # Empêche full numérique
        if value.isnumeric():
            raise serializers.ValidationError(
                "Le nom ne peut pas contenir uniquement des chiffres."
            )

        # Vérifie doublon
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "Cette catégorie existe déjà."
            )

        return value