from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор Пользователя.'''
    class Meta:
        model = User
        fields = '__all__'
