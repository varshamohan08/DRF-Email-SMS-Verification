from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    USER_TYPE_CHOICES = [
        ('User', 'User'),
        ('Admin', 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_details')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, null= True, blank= True)
    dob = models.DateTimeField(null= True, blank= True)
    email = models.EmailField(null= True, blank= True)
    mobile = models.CharField(max_length=15, unique= True, null=True, blank=True)
    bln_verified = models.BooleanField(default=False)
    address = models.TextField(null= True, blank= True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,null= True, blank= True, related_name='updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # print(f"Calling __str__ for {self.user.username}'s Details")
        return f"{self.user.username}'s Details"