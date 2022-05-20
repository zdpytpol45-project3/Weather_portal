import requests
import os

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from pprint import pprint

from .forms import CityForm, CustomUserCreationForm
from .models import City, Location

API_KEY = os.getenv('API_KEY')


def get_city_location(city_name):
    try:
        response_city_coords = requests.get(
            f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=9&appid={API_KEY}'
        )
        get_coords_data = response_city_coords.json()
        if get_coords_data:
            return get_coords_data
        else:
            return None
    except requests.exceptions.HTTPError:
        return HttpResponse("Can't connect with openweather api", status=404)


def get_weather_data_by_location(lat, lon):
    """
    Get weather data from api:
        Current weather
        Hourly forecast for 48 hours
        Daily forecast for 7 days
    """
    try:
        weather_for_location = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=Metric&appid={API_KEY}'
        )
        return weather_for_location.json()
    except requests.exceptions.HTTPError:
        return "Can't connect with openweather api"


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
        By method POST user send location name next to by openweather api app show locations with fit to name.
        User see latitude, longitude, country, state location and by chose one user get information
        about current weather. When user is logged he can save location to his list.
        Check validator that location exist and for logged user that location exist in user's saved cities
    """
    cities_locations = []
    weather_for_new_location = []
    weather_for_user_locations = []
    error_msg_add_city_button = ''
    message_for_user = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_add_city = form.cleaned_data['name']
            request.session['last_add_location'] = new_add_city
            get_location_for_new_city = get_city_location(new_add_city)
            if get_location_for_new_city is None:  # check that city exist in geo api
                error_msg_add_city_button = 'No matching result for specific location'
            else:
                if len(get_location_for_new_city) == 1:
                    add_new_location = True
                else:
                    for counter_cities in range(len(get_location_for_new_city)):

                        state_to_save = get_location_for_new_city[counter_cities].get("state", "--")

                        city_location = {
                            'city': new_add_city,
                            'lat': get_location_for_new_city[counter_cities]['lat'],
                            'lon': get_location_for_new_city[counter_cities]['lon'],
                            'country': get_location_for_new_city[counter_cities]['country'],
                            'state': state_to_save,
                            'number': counter_cities,
                        }
                        cities_locations.append(city_location)
            if error_msg_add_city_button:
                message_for_user = error_msg_add_city_button

    if add_new_location:
        chosen_location = int(chosen_location)
        last_add_location = request.session.get('last_add_location')
        get_location_for_new_city = get_city_location(last_add_location)
        lat_chosen_location = get_location_for_new_city[chosen_location]['lat']
        lon_chosen_location = get_location_for_new_city[chosen_location]['lon']
        if request.user.is_authenticated:
            check_that_location_on_the_same_lat_lon_exist = Location.objects.filter(user=request.user,
                                                                                    lat=lat_chosen_location,
                                                                                    lon=lon_chosen_location).count()
            if check_that_location_on_the_same_lat_lon_exist == 0:
                get_weather_data = get_weather_data_by_location(lat_chosen_location, lon_chosen_location)
                weather_for_new_location = {
                    'location': last_add_location,
                    'country': get_location_for_new_city[chosen_location]['country'],
                    'location_number': chosen_location,
                    'temperature': get_weather_data['current']['temp'],
                    'wind': get_weather_data['current']['wind_speed'],
                    'description': get_weather_data['current']['weather'][0]['description'],
                    'icon': get_weather_data['current']['weather'][0]['icon'],
                }
            else:
                message_for_user = "Location already exist in your list"
                add_new_location = False
        else:
            get_weather_data = get_weather_data_by_location(lat_chosen_location, lon_chosen_location)

            weather_for_new_location = {
                'location': last_add_location,
                'country': get_location_for_new_city[chosen_location]['country'],
                'location_number': chosen_location,
                'temperature': get_weather_data['current']['temp'],
                'wind': get_weather_data['current']['wind_speed'],
                'description': get_weather_data['current']['weather'][0]['description'],
                'icon': get_weather_data['current']['weather'][0]['icon'],
            }

    if request.user.is_authenticated:
        user_locations = Location.objects.filter(user=request.user.id).values()
        for user_locate in user_locations:
            get_weather_data = get_weather_data_by_location(user_locate['lat'], user_locate['lon'])
            weather_for_location = {
                'location_id': user_locate['id'],
                'location': user_locate['name'],
                'country': user_locate['country'],
                'temperature': get_weather_data['current']['temp'],
                'wind': get_weather_data['current']['wind_speed'],
                'description': get_weather_data['current']['weather'][0]['description'],
                'icon': get_weather_data['current']['weather'][0]['icon'],
            }
            weather_for_user_locations.append(weather_for_location)

    form = CityForm()
    context = {
        'weather_for_user_locations': weather_for_user_locations,
        'add_new_location': add_new_location,
        'weather_for_new_location': weather_for_new_location,
        'cities_locations': cities_locations,
        'form': form,
        'message_for_user': message_for_user,
    }
    return render(request, 'weatherapp/yourweather.html', context)


def add_chosen_location(request, chosen_location):
    """
        add_new_location=True: in view your_weather allow to show weather for use and save this location for logged user
    """
    return your_weather(request, add_new_location=True, chosen_location=chosen_location)


def save_chosen_location(request, location, location_number):
    """
        save chosen location for unique authenticated user
    """
    get_location_data_to_save = get_city_location(location)
    name_to_save = location
    lat_to_save = get_location_data_to_save[location_number]['lat']
    lon_to_save = get_location_data_to_save[location_number]['lon']
    country_to_save = get_location_data_to_save[location_number]['country']
    state_to_save = get_location_data_to_save[location_number].get("state", "--")

    data_location_to_save = Location(user=request.user, name=name_to_save, lat=lat_to_save,
                                     lon=lon_to_save, country=country_to_save, state=state_to_save)
    data_location_to_save.save()
    return redirect('weather_in_user_city')


def delete_user_location(request, location_unique_id):
    """
        delete saved location only for authenticated user
    """
    Location.objects.get(id=location_unique_id, user=request.user).delete()
    return redirect('weather_in_user_city')
