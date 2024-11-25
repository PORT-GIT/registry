from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #this is what will help build the token
    #below is the access token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #below is the refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]