from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, User, UserListSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token               # для работы с токеном 
from rest_framework.permissions import IsAuthenticated          # для проыверки авторизован ли пользователь
from rest_framework.generics import ListAPIView


class UserRegistration(APIView):
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


class UserListApiView(ListAPIView):
    def get(self, request):
        queryset = User.objects.values('username')
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)
    