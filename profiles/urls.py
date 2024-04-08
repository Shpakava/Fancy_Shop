from django.urls import path
from profiles.views import *

urlpatterns = [
    path("<slug:profile_slug>", get_profile_details, name='profile_details'),
    path("<slug:profile_slug>/edit", edit_profile_details, name='profile_edit'),
    path("<slug:profile_slug>/fav", get_favorites_list, name='favorites_list'),
    path("<slug:profile_slug>/fav/<int:product_id>", add_to_favorites, name='add_favorites')
]