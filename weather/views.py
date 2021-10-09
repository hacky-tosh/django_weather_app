from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import urllib.request
import json

# jasi = 5472b25182b1d4fa4bf0dffa263255a1

# Create your views here.
def home(request):
    if request.method == 'POST':

        city = request.POST['city']
        # api = "da3b469799e0d01052680ba73cf03d1b"
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=da3b469799e0d01052680ba73cf03d1b').read()

        list_of_data = json.loads(source)

        data = {
            'country_code': str(list_of_data['sys']['country']),
            'cor': str(list_of_data["coord"]["lon"]) + " " + str(list_of_data["coord"]["lat"]),
            'temp': str(list_of_data["main"]['temp']),
            'pressure': str(list_of_data['main']["pressure"]),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data["weather"][0]['main']),
            'description': str(list_of_data["weather"][0]['description']),
            'icon': list_of_data["weather"][0]['icon'],
            'city': city
        }
    else:
        data = {}
    return render(request, 'home.html', data)