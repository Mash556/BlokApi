from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# # Создаем экземпляр DefaultRouter
# router = DefaultRouter()

# # Регистрируем YourModelViewSet в router
# router.register(r'posts', PostModelViewSet, basename='post')

# urlpatterns = [
#     path('', include(router.urls)),
# ]


"""====================filter========================="""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    # path('', include(router.urls)),
    path('', PostListCreateAPIView.as_view())
]