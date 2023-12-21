from rest_framework import generics, permissions, mixins
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

# надо написать СRUD на ModelViewSet
# написать FullCRUD на ModelViewSet(Post)
# n+1 & lazy queryset
    
