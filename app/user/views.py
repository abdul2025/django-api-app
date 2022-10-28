"""
Views for the user apis

"""

from rest_framework import generics

from user.serializers import UserSerializer


class CreateUsersView(generics.CreateApiView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
