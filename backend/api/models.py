from django.db import models
from users.models import User

class Query(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('answered', 'Answered'),
        ('closed', 'Closed'),
    ]

    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queries')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    category = models.CharField(max_length=50)  # e.g., 'crops', 'livestock', 'soil'
    urgency = models.CharField(max_length=20, default='normal')  # low, normal, high

    def __str__(self):
        return f"{self.title} by {self.farmer.username}"

class Consultation(models.Model):
    query = models.OneToOneField(Query, on_delete=models.CASCADE, primary_key=True)
    expert = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultations')
    response = models.TextField()
    responded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_satisfactory = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Consultation for {self.query.title} by {self.expert.username}"

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('guide', 'Guide'),
        ('video', 'Video'),
        ('article', 'Article'),
        ('tool', 'Tool'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='resources/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title