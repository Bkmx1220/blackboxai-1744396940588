from rest_framework import serializers
from .models import User, FarmerProfile, ExpertProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'phone_number', 'location', 'is_farmer', 'is_expert']
        read_only_fields = ['is_farmer', 'is_expert']

class FarmerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = FarmerProfile
        fields = '__all__'

class ExpertProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = ExpertProfile
        fields = '__all__'