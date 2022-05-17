import requests
import os
import dotenv

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from pprint import pprint

from .forms import CityForm, CustomUserCreationForm
from .models import City

API_KEY = os.getenv('API_KEY')


def get_city_location(city_name):
    #http://api.openweathermap.org/geo/1.0/direct?q=London&limit=9&appid=f92692da38455ae53f832ee64b87574c
    try:
        response_city_coords = requests.get(
            f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=9&appid={API_KEY}'
        )
        get_coords_data = response_city_coords.json()
        if get_coords_data:  # check that city exist in geo api
            return get_coords_data
        else:
            return ValueError("No matching result for specific city")
    except requests.exceptions.HTTPError:
        return "Can't connect with openweather api"


def get_weather_data_by_location(lat, lon):
    """
    Get weather data from api:
        Current weather
        Hourly forecast for 48 hours
        Daily forecast for 7 days
    """
    try:
        weather_for_location = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current&appid={API_KEY}'
        )
        return weather_for_location.json()
    except requests.exceptions.HTTPError:
        return "Can't connect with openweather api"


def try_weather(request):
    return render(request, 'weatherapp/tryweather.html')


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


def your_weather(request, add_new_location=False, chosen_location=0):
    """
        Connect with openweather api and show information about weather in choosen city in website
        Saved added city for only logged user
        Check validator that city exist and for logged user that city exist in user's saved cities
    """
    cities_locations = []
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_add_city = form.cleaned_data['name']
            request.session['last_add_location'] = new_add_city
            get_location_for_new_city = get_city_location(new_add_city)
            if 'state' in get_location_for_new_city[0]:
                print('True')
            else:
                print('false')
            if len(get_location_for_new_city) == 1:
                add_new_location = True
            else:
                for counter_cities in range(len(get_location_for_new_city)):
                    if 'state' in get_location_for_new_city[counter_cities]:
                        location_state = get_location_for_new_city[counter_cities]['state']
                    else:
                        location_state = "---"
                    city_location = {
                        'city': new_add_city,
                        'lat': get_location_for_new_city[counter_cities]['lat'],
                        'lon': get_location_for_new_city[counter_cities]['lon'],
                        'country': get_location_for_new_city[counter_cities]['country'],
                        'state': location_state,
                        'number': counter_cities,

                    }
                    cities_locations.append(city_location)


    if add_new_location:
        chosen_location = int(chosen_location)
        last_add_location = request.session.get('last_add_location')
        get_location_for_new_city = get_city_location(last_add_location)
        lat_chosen_location = get_location_for_new_city[chosen_location]['lat']
        lon_chosen_location = get_location_for_new_city[chosen_location]['lon']
        print(lat_chosen_location, "jest typu:", type(lat_chosen_location))
        chosen_unique_location = {
            'location': last_add_location,
            'lat': get_location_for_new_city[chosen_location]['lat'],
            'lon': get_location_for_new_city[chosen_location]['lon'],
        }
        print(last_add_location, 'last added location')
        print(chosen_unique_location)





    form = CityForm()
    context = {
        'cities_locations': cities_locations,
        'form': form,
    }
    return render(request, 'weatherapp/yourweather.html', context)


def add_chosen_location(request, chosen_location):

    return your_weather(request, add_new_location=True, chosen_location=chosen_location)

#    return redirect('weather_in_user_city', chosen_location, add_new_location=False)


def delete_user_city(request, city_name_to_delete):
    """
        delete saved city for unique user
    """
    City.objects.get(name=city_name_to_delete, user=request.user).delete()
    return redirect('weather_in_user_city')


'''def your_weather(request):
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
            if form.is_valid():
                new_add_city = form.cleaned_data['name']
                get_weather_data_for_city = requests.get(url.format(new_add_city)).json()
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
    return render(request, 'weatherapp/yourweather.html', context)'''