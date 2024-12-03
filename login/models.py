from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    phonenumber = models.CharField(max_length=11, unique=True)  # Use CharField for phone numbers
    password = models.CharField(max_length=255)  # For hashed passwords

    def __str__(self):
        return self.username

