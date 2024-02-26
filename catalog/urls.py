from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', index),
    path("category/", categories, name='categories'),
    path("category/<slug:cat>", category, name='category'),
]