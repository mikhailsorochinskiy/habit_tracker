from rest_framework import generics
from .models import UsefulHabit, PleasantHabit
from .serializers import UsefulHabitSerializer, PleasantHabitSerializer
from .paginators import ListPagination
from .permissions import IsOwner, IsAdmin


class ListApiViewUsefulHabit(generics.ListAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    pagination_class = ListPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return UsefulHabit.objects.all()
        return UsefulHabit.objects.filter(is_public=True)


class OwnerListApiViewUsefulHabit(generics.ListAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    pagination_class = ListPagination
    permission_classes = [IsOwner]

    def get_queryset(self):
        return UsefulHabit.objects.filter(owner=self.request.user)


class CreateApiViewUsefulHabit(generics.CreateAPIView):
    serializer_class = UsefulHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save()
        useful_habit.owner = self.request.user
        useful_habit.save()


class RetrieveApiViewUsefulHabit(generics.RetrieveAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class UpdateApiViewUsefulHabit(generics.UpdateAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class DestroyApiViewUsefulHabit(generics.DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class ListApiViewPleasantHabit(generics.ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = ListPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return PleasantHabit.objects.all()
        return PleasantHabit.objects.filter(is_public=True)


class OwnerListApiViewPleasantHabit(generics.ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = ListPagination
    permission_classes = [IsOwner]

    def get_queryset(self):
        return PleasantHabit.objects.filter(owner=self.request.user)


class CreateApiViewPleasantHabit(generics.CreateAPIView):
    serializer_class = PleasantHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save()
        useful_habit.user = self.request.user
        useful_habit.save()


class RetrieveApiViewPleasantHabit(generics.RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class UpdateApiViewPleasantHabit(generics.UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsOwner | IsAdmin]


class DestroyApiViewPleasantHabit(generics.DestroyAPIView):
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsOwner | IsAdmin]
