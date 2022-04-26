import requests
from django.shortcuts import render


# Create your views here.
def your_weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=f92692da38455ae53f832ee64b87574c'

    city = 'Las Vegas'

    get_weather_data = requests.get(url.format(city)).json()

    weather_in_city = {
        'city': city,
        'temperature': get_weather_data['main']['temp'],
        'wind': get_weather_data['wind']['speed'],
        'description': get_weather_data['weather'][0]['description'],
        'icon': get_weather_data['weather'][0]['icon'],
    }

    context = {"weather_in_city": weather_in_city}
    return render(request, 'weatherapp/yourweather.html', context)
