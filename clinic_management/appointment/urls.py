from django.urls import path
from .views import *



urlpatterns = [
    path('', book_appointment, name='book_appointment'),
    path("cloudwatch/alert/", cloudwatch_alert, name="cloudwatch_alert"),
]
