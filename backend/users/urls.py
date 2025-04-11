from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import UserProfileView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]