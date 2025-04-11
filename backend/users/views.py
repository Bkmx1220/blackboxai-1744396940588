from rest_framework import generics, permissions
from .models import User, FarmerProfile, ExpertProfile
from .serializers import UserSerializer, FarmerProfileSerializer, ExpertProfileSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        user = self.request.user
        if user.is_farmer:
            return FarmerProfileSerializer
        elif user.is_expert:
            return ExpertProfileSerializer
        return super().get_serializer_class()