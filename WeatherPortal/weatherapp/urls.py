from django.urls import path, include
from . import views

urlpatterns = [
    path('your-weather/', views.your_weather, name='weather_in_user_city'),
    path('your-weather/delete/<city_name_to_delete>', views.delete_user_city, name='delete_user_city')
]
