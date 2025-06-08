from rest_framework import serializers
from home.models import ReminderModel
from django.contrib.auth.models import User

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReminderModel 
        fields = ['message', 'date', 'time', 'reminder_type']

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]

