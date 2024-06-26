from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    '''Контроллеры на основе дженерик (создание/регистрация Пользователя).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        '''Переопределяем метод для сохр.хешированного пароля в БД.'''
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка Пользователей).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(UpdateAPIView):
    '''Контроллеры на основе дженерик (редактирование Пользователя).'''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserDestroyAPIView(DestroyAPIView):
    '''Контроллеры на основе дженерик (удаление Пользователя).'''
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    