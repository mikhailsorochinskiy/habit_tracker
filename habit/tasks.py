from celery import shared_task
from .services import send_message_tg
from .models import UsefulHabit


@shared_task
def send_message():
    habits = UsefulHabit.objects.filter(owner__isnull=False)
    for habit in habits:
        if habit.owner.chat_id:
            message = f'Напоминание: {habit.action} в {habit.habit_time} в {habit.place}!'
            chat_id = habit.owner.chat_id
            send_message_tg(message, chat_id)
