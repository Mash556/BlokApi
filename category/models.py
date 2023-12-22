from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(
        'self',    # под категория
        on_delete = models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    
