from rest_framework import serializers
from .models import Category 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    # тот метод который  отв за отображение
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        children = instance.children.all()
        if children:
            repr['children'] = CategorySerializer(
                children, many=True
            ).data
            
        repr['makers'] = 'makers'
        return repr 