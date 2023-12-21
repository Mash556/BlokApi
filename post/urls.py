from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/', PostDetailAPIView.as_view()),
    path('', PostListCreateAPIView.as_view())
]