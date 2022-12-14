"""
Serializer for user api View
"""

from django.contrib.auth import (get_user_model, authenticate)

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""


    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}} # this is a way to validate the password against the api.

    def create(self, validated_data):
        """Create a new user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for user auth"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validates and auth users"""
        email = attrs.get('email'),
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username = email,
            password = password,
        )

        if not user:
            msg = _('Unable to validate user with given email and password')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user

        return attrs


