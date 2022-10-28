"""
Tests for user api
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status



CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """ Crreate and return new user"""
    return get_user_model().objects.create_user(**params)



class PublicApiTests(TestCase):
    """ Tests the public feature of the user API"""

    def setUp(self):
        self.client = APIClient()

    def create_user_success(self):
        """Test create user successfull"""
        payload = {
            'email':'test@example.com',
            'password':'test123',
            'name':'testName',
        }
        res = self.client.post(CREATE_USER_URL, payload=payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(emai=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test Error returned if user with email existed"""
        payload = {
            'email':'test@example.com',
            'password':'test123',
            'name':'testName',
            }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password is too short"""

        payload = {
            'email':'test@example.com',
            'password':'test123',
            'name':'testName',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email'],
        ).exists()
        self.assertFalse(user_exists)



