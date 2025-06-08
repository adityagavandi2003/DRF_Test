from django.urls import path
from home.views import ReminderCreateView,RegisterUserView,DisplayReminder
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("reminder/",DisplayReminder.as_view(),name='reminder'),
    path('reminder/create/',ReminderCreateView.as_view(),name='create-reminder'),

    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
