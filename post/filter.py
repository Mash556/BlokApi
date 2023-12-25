import django_filters
from .models import Post

class PostModelFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']