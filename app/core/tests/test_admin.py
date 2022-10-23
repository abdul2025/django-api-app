"""
Test for django admin modifications


"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client



class AdminSiteTests(TestCase):
    """Test admin modifications"""
    def setUp(self) -> None:
        """create user and client"""
        self.client = Client
        self.admin_user = get_user_model().objects.create_superuser(email='test@gmail.com', password='123123')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email ='test@gmail.com', password = '123123', name= 'home' )

    def test_users_list(self):
        """Test That users are listed on the page"""
        url = ('admin:core.user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

