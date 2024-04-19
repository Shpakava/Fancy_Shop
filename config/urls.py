"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from catalog.views import page_not_found, ShopHome, about, search
from profiles.views import register_user, login_user, logout_user

urlpatterns = [
    path('', ShopHome.as_view(), name="home"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('profile/', include('profiles.urls')),
    path('cart/', include('cart.urls', namespace="cart")),
    path('order/', include('orders.urls', namespace="orders")),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('search/', search, name="search_result"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = page_not_found