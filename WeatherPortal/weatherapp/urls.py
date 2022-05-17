from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('your-weather/', views.your_weather, name='weather_in_user_city'),
    path('your-weather/delete/<city_name_to_delete>', views.delete_user_city, name='delete_user_city'),
    path('try-weather/', views.try_weather),
    path('your-weather/add_location/<chosen_location>', views.add_chosen_location, name='add_chosen_location')
]
