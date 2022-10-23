from django.db import models  # noqa
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.

class UserManager(BaseUserManager):
    """Manager for Users"""
    def create_user(self, email, password=None, **extra_fields):
        """Create a new User"""
        if not email:
            raise ValueError("Please provide an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, password=None, **extra_fields):
        """Create a super User"""
        if not email:
            raise ValueError("Please provide an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)


        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'

