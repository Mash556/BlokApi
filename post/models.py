from django.db import models
from category.models import Category
# from django.contrib.au 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True,)
    body = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name = 'posts',
        on_delete = models.CASCADE
    )
    image = models.ImageField(upload_to='images/', null=True)     # для добавление картинки 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_at']       # отвечает за порядок хранение данных


