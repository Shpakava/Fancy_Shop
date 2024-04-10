from django.urls import path
from catalog.views import *

urlpatterns = [
    # path("", ShopHome.as_view(), name='categories'),
    path("<slug:category_slug>", category, name='category'),
    path("<slug:category_slug>/<slug:product_slug>", ProductDetail.as_view(), name='product_detail'),
]