from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# Создаем экземпляр DefaultRouter
router = DefaultRouter()

# Регистрируем YourModelViewSet в router
router.register(r'posts', PostModelViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]