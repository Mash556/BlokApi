from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, User, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token               # для работы с токеном 
from rest_framework.authtoken.models import Token            # для работы с токеном 
from rest_framework.permissions import IsAuthenticated  , IsAdminUser         # для проыверки авторизован ли пользователь
from rest_framework import generics                # generic это готовая логика которая работает с 


class UserRegistration(APIView):
    """Регистрация на базу"""
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Account is created', status=200)
    

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)    # либо создает либо получает токен

        response_data = {
            'token': token.key,
            'username': user.username,
            'id': user.id
        }
        return  Response(response_data)


class LogautView(APIView):    # для удаление токена
    permission_classes = [IsAuthenticated]    # проверяет на наличие токена

    def post(self, request):
        user = request.user       #   
        Token.objects.filter(user=user).delete()    # получаем 'тот токен и его удаляем 
        return Response(
            'Успешно вышли с аккаунта'
        )
    


# написать UserListApiView на generics
# запрос возвращает всех сущ пользователей  


class UserListApiView(generics.ListAPIView):
    """Тут хранится список всех user"""
    queryset = User.objects.values('username')
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsAdminUser]

