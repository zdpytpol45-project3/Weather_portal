from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('your-weather/', views.your_weather, name='weather_in_user_city'),
    path('your-weather/delete_location/<location_unique_id>', views.delete_user_location, name='delete_user_location'),
    path('your-weather/add_location/<chosen_location>', views.add_chosen_location, name='add_chosen_location'),
    path('your-weather/save_location/<location>/<int:location_number>/',
         views.save_chosen_location, name='save_chosen_location'),
]
