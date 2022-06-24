from rest_framework import serializers
from django.apps import apps
StudentAnswer = apps.get_model('quiz', 'StudentAnswer')

class StudentAudioAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = '__all__'