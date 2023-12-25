from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.viewsets import ModelViewSet
import django_filters
from post.filters import PostModelFilter
from .serializers import PostSerializer
from .models import Post
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class StandartResultPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['title', 'body']
    filterset_fields = ['category']
    # filterset_class = PostModelFilter

    def perform_create(self, serializer):
        posts = Post.objects.select_related('category')
        for post in posts:
            print(post.category)
        
        serializer.save(owner=self.request.user)

        
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search_query = self.request.query_params.get('search', None)
    #     # query_params = {'search':'asdf', 'category':1}
    #     if search_query:
    #         queryset = queryset.filter(title__icontains=search_query)
    #         # ILIKE %search_query%
    #     return queryset

    


# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     lookup_field = 'id'
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
    

# написать FullCRUD на ModelViewSet(Post)
# n+1 & lazy queryset
# mixins | generics
# написать логику поиска и филтрации для постов
# написать кастомный permission который проверяет поле is_staff| staff status