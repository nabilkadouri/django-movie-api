from rest_framework import serializers
from django.utils import timezone

from movies.models import Actor


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = "__all__"

    def validate_first_name(self, value):

        # Nettoyage
        value = value.strip()

        # Vérifie vide
        if not value:
            raise serializers.ValidationError(
                "Le nom de l'acteur ne doit pas être vide."
            )

        # Vérifie uniquement numérique
        if value.isdigit():
            raise serializers.ValidationError(
                "Le nom de l'acteur ne doit pas contenir que des nombres."
            )

        # Vérifie longueur minimale
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le nom de l'acteur doit contenir au moins 3 caractères."
            )

        # Formatage final
        value = value.title()

        return value

    def validate_last_name(self, value):

        # Nettoyage
        value = value.strip()

        # Vérifie vide
        if not value:
            raise serializers.ValidationError(
                "Le prénom de l'acteur ne doit pas être vide."
            )

        # Vérifie uniquement numérique
        if value.isdigit():
            raise serializers.ValidationError(
                "Le prénom de l'acteur ne doit pas contenir que des nombres."
            )

        # Vérifie longueur minimale
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le prénom de l'acteur doit contenir au moins 3 caractères."
            )

        # Formatage final
        value = value.title()

        return value

    def validate_birth_date(self, value):

        current_date = timezone.now().date()

        # Vérifie date future
        if value > current_date:
            raise serializers.ValidationError(
                "La date d'anniversaire de l'acteur ne doit pas être dans le futur."
            )

        return value