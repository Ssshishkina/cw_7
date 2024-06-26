from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from habits.models import Habit
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


# Create your views here.
class HabitCreateAPIView(CreateAPIView):
    '''Контроллеры на основе дженерик (создание Привычки).'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitDetailAPIView(RetrieveAPIView):
    '''Контроллеры на основе дженерик (просмотр Привычки).'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitListAPIView(ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка Привычек).'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)


class HabitUpdateAPIView(UpdateAPIView):
    '''Контроллеры на основе дженерик (редактирование Привычки).'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(DestroyAPIView):
    '''Контроллеры на основе дженерик (удаление Привычки).'''
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class PublicHabitListApiView(ListAPIView):
    '''Контроллеры на основе дженерик (просмотр списка Публичных Привычек).'''
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    