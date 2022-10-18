"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):
    """Test for models User"""

    def test_create_user_with_email_successfull(self):
        """Test create user with email successfull"""
        email = 'testEmail@gmail.com'
        password = 'testPassword'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email normalization"""
        simple_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in simple_emails:
            user = get_user_model().objects.create_user(email, '1233simple')
            self.assertEqual(user.email, expected)