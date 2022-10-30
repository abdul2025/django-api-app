"""
URL mapping for user views

"""


from django.urls import path
from user import views

app_name = 'user'


urlpatterns = [
    path('create/', views.CreateUsersView.as_view(), name='create'),
    path('token/', views.CreateTokenViews.as_view(), name='token'),
]
