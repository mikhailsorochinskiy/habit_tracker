from django.urls import path
from .views import (ListApiViewUsefulHabit, ListApiViewPleasantHabit, CreateApiViewUsefulHabit,
                    CreateApiViewPleasantHabit, RetrieveApiViewPleasantHabit, RetrieveApiViewUsefulHabit,
                    UpdateApiViewUsefulHabit, UpdateApiViewPleasantHabit, DestroyApiViewPleasantHabit,
                    DestroyApiViewUsefulHabit)


app_name = 'habit'

urlpatterns = [
    path('useful_habits/', ListApiViewUsefulHabit.as_view(), name='useful_habits'),
    path('useful_habit/create/', CreateApiViewUsefulHabit.as_view(), name='useful_habit_create'),
    path('useful_habit/<int:pk>/', RetrieveApiViewUsefulHabit.as_view(), name='useful_habit'),
    path('useful_habit/<int:pk>/update/', UpdateApiViewUsefulHabit.as_view(), name='useful_habit_update'),
    path('useful_habit/<int:pk>/delete/', DestroyApiViewUsefulHabit.as_view(), name='useful_habit_delete'),

    path('pleasant_habits/', ListApiViewPleasantHabit.as_view(), name='pleasant_habits'),
    path('pleasant_habit/create/', CreateApiViewPleasantHabit.as_view(), name='pleasant_habit_create'),
    path('pleasant_habit/<int:pk>/', RetrieveApiViewPleasantHabit.as_view(), name='pleasant_habit'),
    path('pleasant_habit/<int:pk>/update/', UpdateApiViewPleasantHabit.as_view(), name='pleasant_habit_update'),
    path('pleasant_habit/<int:pk>/delete/', DestroyApiViewPleasantHabit.as_view(), name='pleasant_habit_delete'),
]
