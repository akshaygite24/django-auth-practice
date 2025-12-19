from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete=models.CASCADE delete post if user is being deleted
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Set the date & time ONLY ONCE — when the object is created
    updated_at = models.DateTimeField(auto_now=True) # Update the date & time EVERY TIME the object is saved
    
    def __str__(self):
        return self.title + "\n" + self.description     # if we print post we can see this