from django.db import models
from datetime import datetime

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=200)
    email = models.EmailField("email", max_length=200)
    nickname = models.CharField("nickname", max_length=100, default="")
    dogname = models.CharField("dogname", max_length=100, default="")
