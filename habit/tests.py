from rest_framework.test import APITestCase
from .models import UsefulHabit, PleasantHabit
from users.models import User
from django.urls import reverse
from rest_framework import status

class UsefulHabitAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.useful_habit = UsefulHabit.objects.create(owner=self.user, habit_time='12:00:00', action='test',
                                                       time_to_complete=10)
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        url = reverse('habit:useful_habit', args=[self.useful_habit.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('action'), self.useful_habit.action)
        self.assertFalse(response.data.get('award'))
        self.assertFalse(response.data.get('pleasant_habit'))

    def test_create(self):
        url = reverse('habit:useful_habit_create')
        data = {
            "habit_time": "13:00:00",
            "action": 'test_2',
            'time_to_complete': 10
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UsefulHabit.objects.all().count(), 2)

    def test_create_time_to_complete_error(self):
        url = reverse('habit:useful_habit_create')
        data = {
            "habit_time": "13:00:00",
            "action": 'test_2',
            'time_to_complete': 130
        }
        response = self.client.post(url, data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_award_and_pleasant(self):
        pleasant_habit = PleasantHabit.objects.create(owner=self.user, habit_time='12:00:00', action='test',
                                                       time_to_complete=10)
        url = reverse('habit:useful_habit_create')
        data = {
            "habit_time": "13:00:00",
            "action": 'test_2',
            'time_to_complete': 100,
            'award': 'test',
            'pleasant_habit': pleasant_habit
        }
        response = self.client.post(url, data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_frequency_error(self):
        url = reverse('habit:useful_habit_create')
        data = {
            "habit_time": "13:00:00",
            "action": 'test_2',
            'time_to_complete': 10,
            'frequency': 8
        }
        response = self.client.post(url, data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update(self):
        url = reverse('habit:useful_habit_update', args=[self.useful_habit.pk])
        data = {
            "time_to_complete": 12
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('time_to_complete'), 12)
        self.assertEqual(response.data.get('frequency'), 1)

    def test_delete(self):
        url = reverse('habit:useful_habit_delete', args=[self.useful_habit.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UsefulHabit.objects.all().count(), 0)

    def test_list(self):
        url = reverse('habit:useful_habits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UsefulHabit.objects.all().count(), 1)

    def test_owner_list(self):
        url = reverse('habit:my_useful_habits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UsefulHabit.objects.all().count(), 1)


class PleasantHabitAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.useful_habit = PleasantHabit.objects.create(owner=self.user, habit_time='12:00:00', action='test',
                                                       time_to_complete=10)
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        url = reverse('habit:pleasant_habit', args=[self.useful_habit.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('action'), self.useful_habit.action)

    def test_create(self):
        url = reverse('habit:pleasant_habit_create')
        data = {
            "habit_time": "13:00:00",
            "action": 'test_2',
            'time_to_complete': 10
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PleasantHabit.objects.all().count(), 2)

    def test_update(self):
        url = reverse('habit:pleasant_habit_update', args=[self.useful_habit.pk])
        data = {
            "time_to_complete": 12
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('time_to_complete'), 12)

    def test_delete(self):
        url = reverse('habit:pleasant_habit_delete', args=[self.useful_habit.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PleasantHabit.objects.all().count(), 0)

    def test_list(self):
        url = reverse('habit:pleasant_habits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PleasantHabit.objects.all().count(), 1)

    def test_owner_list(self):
        url = reverse('habit:my_pleasant_habits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PleasantHabit.objects.all().count(), 1)
