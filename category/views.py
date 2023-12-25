from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_permissions(self):
    #     if self.request.method in ['POST', 'PATCH', 'PUT', 'DELETE']:
    #         return [permissions.IsAdminUser(), ]
    #     return [permissions.AllowAny()]
    

