from rest_framework import generics
from .models import UsefulHabit, PleasantHabit
from .serializers import UsefulHabitSerializer, PleasantHabitSerializer


"""полезные привычки"""
class ListApiViewUsefulHabit(generics.ListAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()


class CreateApiViewUsefulHabit(generics.CreateAPIView):
    serializer_class = UsefulHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save()
        useful_habit.user = self.request.user
        useful_habit.save()

class RetrieveApiViewUsefulHabit(generics.RetrieveAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()


class UpdateApiViewUsefulHabit(generics.UpdateAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()


class DestroyApiViewUsefulHabit(generics.DestroyAPIView):
    queryset = UsefulHabit.objects.all()


"""приятные привычки"""
class ListApiViewPleasantHabit(generics.ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()


class CreateApiViewPleasantHabit(generics.CreateAPIView):
    serializer_class = PleasantHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save()
        useful_habit.user = self.request.user
        useful_habit.save()

class RetrieveApiViewPleasantHabit(generics.RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()


class UpdateApiViewPleasantHabit(generics.UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()


class DestroyApiViewPleasantHabit(generics.DestroyAPIView):
    queryset = PleasantHabit.objects.all()
