from django.shortcuts import render
from .models import Forecast

app_name = 'weather'

def index(request):
    forecasts = Forecast.objects.all()
    context = {
        'forecasts': forecasts
    }
    return render(request, 'weather/index.html', context)