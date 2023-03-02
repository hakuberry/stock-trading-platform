"""
URL mappings for the funds app
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from funds import views


router = DefaultRouter()
router.register('funds', views.FundsViewSet)

app_name = 'funds'

urlpatterns = [
    path('', include(router.urls)),
]
