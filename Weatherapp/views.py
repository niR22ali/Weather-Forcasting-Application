from django.shortcuts import render
import requests
import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def weathersystem(request):
    place = request.POST.get('place','toronto')
    # place = 'Lucknow'
    url   = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid=6f8f73ca9eebf882f90c1333433118ac'
    info  = requests.get(url).json()

    weather_info = {
        'place': info['name'],
        'weather': info['weather'][0]['main'],
        'icon': info['weather'][0]['icon'],
        # 'kelvin_temperature': info['main']['temp'],
        'celcius_temperature': int(info['main']['temp']-273),
        'pressure': info['main']['pressure'],
        'humidity': info['main']['humidity'],
        'description': info['weather'][0]['description']
    }

    context = {'info': weather_info}
    return render(request, 'weathersystem.html', context)





    # if 'place' in request.POST:
    #     place = request.POST['place']
    # else:
    #     place = 'Amsterdam'
    #
    # appid = '6f8f73ca9eebf882f90c1333433118ac'
    # urlss = 'https://api.openweathermap.org/data/2.5/weather'
    # # 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=6f8f73ca9eebf882f90c1333433118ac'
    # PARA = {'q':'place', 'appid':appid, 'units':'metric' }
    # resp = requests.get(url=urlss, params=PARA)
    # weather_info = resp.json()
    # description = weather_info['weather'][0]['description']
    # icon = weather_info['weather'][0]['icon']
    # temp = weather_info['main']['temp']
    # country = weather_info['sys']['country']
    # dayMonYr = datetime.date.today()



    # return render(request, 'weathersystem.html', {'description': description, 'temp': temp, 'icon': icon,
    #                                               'dayMonYr': dayMonYr, 'place': place, 'country': country})