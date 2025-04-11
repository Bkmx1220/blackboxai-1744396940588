from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import (
    RegisterView,
    LoginView,
    QueryListCreateView,
    QueryDetailView,
    ConsultationCreateView,
    ResourceListView,
    ExpertListView
)

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Queries
    path('queries/', QueryListCreateView.as_view(), name='query-list'),
    path('queries/<int:pk>/', QueryDetailView.as_view(), name='query-detail'),
    
    # Consultations
    path('consultations/', ConsultationCreateView.as_view(), name='consultation-create'),
    
    # Resources
    path('resources/', ResourceListView.as_view(), name='resource-list'),
    
    # Experts
    path('experts/', ExpertListView.as_view(), name='expert-list'),
]