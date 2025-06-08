from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class ReminderModel(models.Model):
    REMINDER_CHOICES = (
        ("email","Email"),
        ("sms","SMS")
    )

    id = models.CharField(default=uuid4(),max_length=50,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    reminder_type = models.CharField(max_length=10,choices=REMINDER_CHOICES)
    isremind = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reminder_type.upper()} Reminder at {self.date} {self.time}"