"""
Serializers for the funds API View.
"""
from rest_framework import serializers
from core.models import Funds


class FundsSerializer(serializers.ModelSerializer):
    """Serializer for the funds object."""

    class Meta:
        model = Funds
        fields = '__all__'
