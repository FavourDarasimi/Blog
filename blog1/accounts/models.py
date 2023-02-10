from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


class Profile(models.Model):
    Gender=(
        ("1","Male"),
        ("2","Female")
    )

    user=models.OneToOneField('auth.User',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=15,choices=Gender,default='1')
    bio=models.TextField(max_length=200)
    picture=models.ImageField(upload_to="image/")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile", kwargs={'pk':self.pk})


    


# Create your models here.
