"""tp_furnitures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import path, include

from tp.viewsets import FurnitureViewSet, ShopViewSet, ShopOwnerViewSet

router = SimpleRouter()
router.register('furnitures', FurnitureViewSet, basename='furniture')
router.register('shops', ShopViewSet, basename='shop')
router.register('owners', ShopOwnerViewSet, basename='owner')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
