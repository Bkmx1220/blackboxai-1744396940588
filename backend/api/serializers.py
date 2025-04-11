from rest_framework import serializers
from users.models import User, FarmerProfile, ExpertProfile
from .models import Query, Consultation, Resource

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'phone_number', 'location', 'is_farmer', 'is_expert']

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

class QuerySerializer(serializers.ModelSerializer):
    farmer = UserSerializer(read_only=True)
    
    class Meta:
        model = Query
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'status']

class ConsultationSerializer(serializers.ModelSerializer):
    query = QuerySerializer(read_only=True)
    expert = UserSerializer(read_only=True)
    
    class Meta:
        model = Consultation
        fields = '__all__'
        read_only_fields = ['responded_at', 'updated_at']

class ResourceSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Resource
        fields = '__all__'
        read_only_fields = ['created_at']