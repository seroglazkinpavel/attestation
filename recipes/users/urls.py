from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
]