"""
Views for the funds APIs
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Funds
from funds import serializers


class FundsViewSet(viewsets.ModelViewSet):
    """View for manage portfolio APIs."""
    serializer_class = serializers.FundsSerializer
    queryset = Funds.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve funds for authenticated user."""
        return self.queryset.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        """Create new funds"""
        serializer.save(user=self.request.user)
