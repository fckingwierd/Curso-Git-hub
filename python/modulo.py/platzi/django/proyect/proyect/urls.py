from django.urls import path
from files import exercise

urlpatterns = [
    path('hello-world/', exercise.hi)
]
