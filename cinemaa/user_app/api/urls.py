from django.contrib import admin
from django.urls import path,include
from user_app.api.views import registration_view


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view,name='register'),
]

