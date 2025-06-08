from django.contrib import admin
from home.models import ReminderModel
# Register your models here.

@admin.register(ReminderModel)
class ReminderModelAdmin(admin.ModelAdmin):
    list_display = ["message","time","date","reminder_type","user","isremind","created_at"]