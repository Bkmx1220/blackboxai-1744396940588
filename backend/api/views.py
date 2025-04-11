from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Query, Consultation, Resource
from .serializers import (
    UserSerializer,
    FarmerProfileSerializer,
    ExpertProfileSerializer,
    QuerySerializer,
    ConsultationSerializer,
    ResourceSerializer
)
from users.models import User, FarmerProfile, ExpertProfile

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Create profile based on user type
            if user.is_farmer:
                FarmerProfile.objects.create(user=user)
            elif user.is_expert:
                ExpertProfile.objects.create(user=user)
                
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class QueryListCreateView(generics.ListCreateAPIView):
    serializer_class = QuerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_farmer:
            return Query.objects.filter(farmer=user)
        elif user.is_expert:
            return Query.objects.filter(status='pending')
        return Query.objects.none()

    def perform_create(self, serializer):
        if self.request.user.is_farmer:
            serializer.save(farmer=self.request.user)

class QueryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_expert:
            serializer.save(expert=self.request.user)

class ResourceListView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ExpertListView(generics.ListAPIView):
    queryset = ExpertProfile.objects.filter(user__is_expert=True)
    serializer_class = ExpertProfileSerializer
    permission_classes = [permissions.AllowAny]