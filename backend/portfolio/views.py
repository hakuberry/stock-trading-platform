"""
Views for the portfolio APIs
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Portfolio
from recipe import serializers


class PortfolioViewSet(viewsets.ModelViewSet):
    """View for manage portfolio APIs."""
    serializer_class = serializers.PortfolioSerializer
    queryset = Portfolio.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve portfolios for authenticated user."""
        return self.queryset.filter(user=self.request.user).all()
