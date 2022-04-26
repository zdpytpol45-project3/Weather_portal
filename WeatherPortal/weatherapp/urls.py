from django.urls import path, include
from . import views

urlpatterns = [
    path('your-weather/', views.your_weather),
]
