import requests
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CityForm, CustomUserCreationForm
from .models import City


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('weather_in_user_city'))


def your_weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=f92692da38455ae53f832ee64b87574c'

    error_msg_add_city_button = ''
    message_for_user = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_add_city = form.cleaned_data['name']
            existing_new_city_name = City.objects.filter(name=new_add_city).count()
            if existing_new_city_name == 0:
                get_weather_data = requests.get(url.format(new_add_city)).json()
                if get_weather_data['cod'] == 200:
                    form.save()
                else:
                    error_msg_add_city_button = 'City not existing in the world'
            else:
                error_msg_add_city_button = 'City already existing in your list'

        if error_msg_add_city_button:
            message_for_user = error_msg_add_city_button
        else:
            message_for_user = 'New City added successfully'

    form = CityForm()
    cities = City.objects.all()

    cities_for_weather_data = []

    for city in cities:
        get_weather_data = requests.get(url.format(city)).json()

        weather_in_city = {
            'city': city.name,
            'temperature': get_weather_data['main']['temp'],
            'wind': get_weather_data['wind']['speed'],
            'description': get_weather_data['weather'][0]['description'],
            'icon': get_weather_data['weather'][0]['icon'],
        }

        cities_for_weather_data.append(weather_in_city)

    context = {
        "cities_for_weather_data": cities_for_weather_data,
        'form': form,
        'message_for_user': message_for_user,
    }
    return render(request, 'weatherapp/yourweather.html', context)


def delete_user_city(request, city_name_to_delete):
    City.objects.get(name=city_name_to_delete).delete()
    return redirect('weather_in_user_city')
