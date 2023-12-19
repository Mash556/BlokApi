from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate    # для проверки есть ли юзер в нашей бд

class RegisterSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    password=serializers.CharField(required=True, min_length=8, write_only=True)
    password_confirmation=serializers.CharField(required=True, min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['username', 'email', 
                'first_name', 'last_name', 
                'password', 'password_confirmation']
        
    def validate(self, attrs):
        password_confirmation = attrs.pop('password_confirmation')
        if password_confirmation != attrs['password']:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        if not attrs['first_name'].istitle():
            raise serializers.ValidationError(
                'Имя должно начинаться с заглавной буквы'
            )
        return attrs  
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField() # получаем 
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        request = self.context.get('request')   # сюда попадает request из views  
        if username and password:          
            user = authenticate(                #  для получение таких юзеров
                username=username,
                password=password,
                request=request
                )
            if not user:
                raise serializers.ValidationError(           
                    'не правильный пароль или юзернейм'
                )
        else:
            raise serializers.ValidationError(
                'Вы забыли заполнить username или password'
            )
        
        data['user'] = user     #   изменяем значение data под ключом user на новое 
        return data
    
    def validate_username(self, username):    # проверка на того что есть ли такой 
        if not User.objects.filter(username=username).exists():    # проверка на наличие exsists() возвр бул тип данных
            raise serializers.ValidationError(
                'username not found'
            )
        return username
    



class UserListSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)  # Замените на тип вашего поля и его параметры

    class Meta:
        fields = ('username',)