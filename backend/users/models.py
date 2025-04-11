from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    farm_size = models.CharField(max_length=50, blank=True)
    crops = models.CharField(max_length=200, blank=True)
    livestock = models.CharField(max_length=200, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Farmer Profile"

class ExpertProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField(blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    certification = models.CharField(max_length=100, blank=True)
    available_for_consultation = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username}'s Expert Profile"