from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from datetime import datetime

from catalog.models import Product


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    phone_number = models.CharField(verbose_name="Phone", max_length=50, blank=True)
    shipping_address = models.CharField(verbose_name="Address", max_length=100, blank=True)
    postcode = models.CharField(verbose_name="Postcode", max_length=50, blank=True)
    city = models.CharField(verbose_name="City", max_length=100, blank=True)
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=200)
    email = models.EmailField("email", max_length=200)
    nickname = models.CharField("nickname", max_length=100, default="")
    avatar = models.ImageField("Avatar", upload_to="users/", default="default_user.png")
    slug = AutoSlugField(max_length=100, populate_from=('nickname',))
    favorites = models.ManyToManyField(Product, blank=True, default=None, related_name="fav_product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_slug": self.slug, "category_slug": self.category.slug})

    def __str__(self):
        return f"{self.pk} - {self.user.username}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"