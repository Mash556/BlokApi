from django.urls import path 
from .views import *

urlpatterns = [
    path('register/', UserRegistration.as_view()),
    path('login/', LoginView.as_view()),
    path('logaut/', LogautView.as_view()),
    path('<int:id>/', UserDetailAPIView.as_view()),
    path('', UserListApiView.as_view()),
]


