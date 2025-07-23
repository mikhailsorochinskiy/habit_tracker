from django.db import models
from django.conf import settings


class PleasantHabit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=150, blank=True, null=True, verbose_name='место')
    habit_time = models.TimeField(verbose_name='время для выполнения привычки', blank=True, null=True)
    action = models.CharField(max_length=150, verbose_name='действие')
    frequency = models.IntegerField(verbose_name='периодичность', blank=True, null=True, default=1)
    time_to_complete = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(verbose_name='признак публичности', default=False)

    def __str__(self):
        return f'{self.action} в {self.habit_time} в {self.place}'

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'


class UsefulHabit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=150, blank=True, null=True, verbose_name='место')
    habit_time = models.TimeField(verbose_name='время для выполнения привычки')
    action = models.CharField(max_length=150, verbose_name='действие')
    frequency = models.IntegerField(verbose_name='периодичность в днях', default=1)
    time_to_complete = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(verbose_name='признак публичности', default=False)
    pleasant_habit = models.ForeignKey(PleasantHabit, on_delete=models.SET_NULL, blank=True, null=True)
    award = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.action} в {self.habit_time} в {self.place}'

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'
