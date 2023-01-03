from django.urls import path
from . import views

urlpatterns=[
    path('country_info/',views.say_hi)
]