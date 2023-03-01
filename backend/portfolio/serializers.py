"""
Serializers for the portfolio API View.
"""
from rest_framework import serializers
from core.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    """Serializer for the portfolio object."""

    class Meta:
        model = Portfolio
        fields = '__all__'
