from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):

    url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOURAPI'
    
    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
    
    form=CityForm()
    
    cities=City.objects.all()
    
    wd=[]
    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : '25',
            'description' : 'clear',
            'icon' : '',
        }

        wd.append(city_weather)

    context = {'wd' : wd, 'form' : form}
    return render(request, 'weather/index.html', context)