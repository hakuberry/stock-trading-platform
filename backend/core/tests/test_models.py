"""
Tests for models
"""
from unittest.mock import patch
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def create_user(email='user@example.com', password='testpass123'):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user wihtout an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')
    
    def test_create_portfolio(self):
        """Test creating a portfolio is successful"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )

        portfolio = models.Portfolio.objects.create(
            owner=user,
            symbol='ABCD',
            company='ABCD Company',
            transaction='buy',
            quantity=4000,
            price=Decimal('5.50'),
            created_at='2023-10-01:23:11:09',
        )

        self.assertEqual(str(portfolio), portfolio.symbol)

    def test_create_fund(self):
        """Test create a fund is successful"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )

        funds = models.Funds.objects.create(
            owner=user,
            transactionType='deposit',
            amount=Decimal('40000'),
            total=Decimal('70000'),
            created_at='2023-10-01:23:11:09',
        )