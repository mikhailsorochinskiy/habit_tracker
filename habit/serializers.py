from rest_framework import serializers
from .models import UsefulHabit, PleasantHabit


def validate_less_than_120(value):
    if value > 120:
        raise serializers.ValidationError("Значение должно быть не более 120.")


class UsefulHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulHabit
        fields = '__all__'
        extra_kwargs = {'time_to_complete': {'validators': [validate_less_than_120]}}

    def validate(self, attrs):
        pleasant_habit = attrs.get('pleasant_habit')
        award = attrs.get('award')

        if pleasant_habit and award:
            raise serializers.ValidationError(
                "Только одно из полей связанной привычки или вознаграждения может быть заполнено."
            )

        return attrs


class PleasantHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PleasantHabit
        fields = '__all__'
        extra_kwargs = {'time_to_complete': {'validators': [validate_less_than_120]}}
