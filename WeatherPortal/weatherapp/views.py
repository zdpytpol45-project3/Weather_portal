import requests
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from pprint import pprint

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
    """
        Connect with openweather api and show information about weather in choosen city in website
        Saved added city for only logged user
        Check validator that city exist and for logged user that city exist in user's saved cities
    """
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=f92692da38455ae53f832ee64b87574c'
    error_msg_add_city_button = ''
    message_for_user = ''
    cities_for_weather_data = []

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CityForm(request.POST)
            pprint(form)
            if form.is_valid():
                new_add_city = form.cleaned_data['name']
                get_weather_data_for_city = requests.get(url.format(new_add_city)).json()
                pprint(get_weather_data_for_city)
                if get_weather_data_for_city['cod'] == 200:
                    new_city_for_logged_user = City.objects.filter(name=new_add_city, user=request.user).count()
                    if new_city_for_logged_user == 0:
                        form = City(name=new_add_city, user=request.user)
                        form.save()
                    else:
                        error_msg_add_city_button = 'City already existing in your list'
                else:
                    error_msg_add_city_button = 'City not existing in the world'

            if error_msg_add_city_button:
                message_for_user = error_msg_add_city_button
            else:
                message_for_user = 'New City added successfully'

        cities_for_user = City.objects.filter(user=request.user.id)
        for city in cities_for_user:
            get_weather_data = requests.get(url.format(city)).json()

            weather_in_city = {
                'city': city.name,
                'temperature': get_weather_data['main']['temp'],
                'wind': get_weather_data['wind']['speed'],
                'description': get_weather_data['weather'][0]['description'],
                'icon': get_weather_data['weather'][0]['icon'],
            }

            cities_for_weather_data.append(weather_in_city)

    else:
        if request.method == 'POST':
            form = CityForm(request.POST)
            if form.is_valid():
                new_add_city_for_not_logged = form.cleaned_data['name']
                get_weather_data = requests.get(url.format(new_add_city_for_not_logged)).json()
                if get_weather_data['cod'] == 200:
                    cities_for_weather_data = [{
                        'city': new_add_city_for_not_logged,
                        'temperature': get_weather_data['main']['temp'],
                        'wind': get_weather_data['wind']['speed'],
                        'description': get_weather_data['weather'][0]['description'],
                        'icon': get_weather_data['weather'][0]['icon'],
                    }]
                else:
                    error_msg_add_city_button = 'City not existing in the world'
            if error_msg_add_city_button:
                message_for_user = error_msg_add_city_button
            else:
                message_for_user = 'New City added successfully'

    form = CityForm()
    context = {
        "cities_for_weather_data": cities_for_weather_data,
        'form': form,
        'message_for_user': message_for_user,
    }
    return render(request, 'weatherapp/yourweather.html', context)


def delete_user_city(request, city_name_to_delete):
    """
        delete saved city for unique user
    """
    City.objects.get(name=city_name_to_delete, user=request.user).delete()
    return redirect('weather_in_user_city')
