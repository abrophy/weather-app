import requests
import datetime
from django.core.management.base import BaseCommand, CommandError
from weather.models import Forecast

class Command(BaseCommand):
    help = 'fetches weather data for Cape Town from weather24'

    def handle(self, *args, **options):
        url = "http://weather.news24.com/ajaxpro/Weather.Code.Ajax,Weather.ashx"
        headers = {
            'Referer': 'http://weather.news24.com/sa/capetown',
            'Origin': 'http://weather.news24.com',
            'credentials':'include',
            'referrerPolicy': 'no-referrer-when-downgrade',
            'X-AjaxPro-Method': 'GetForecast15DayExpanded',
        }
        body = {
            'cityId': '77107'
        }
        data = requests.post(url, headers=headers, data='{"cityId":"77107"}')
        received_forecast_data = data.json()['value']['Forecasts']

        forecast = received_forecast_data[0]
        date_string = forecast['Date'][6:-2]

        forecast_date = datetime.date.fromtimestamp(int(date_string) / 1000)
        forecast_min_temp = int(forecast['LowTemp'])
        forecast_max_temp = int(forecast['HighTemp'])
        forecast_wind_speed = int(forecast['WindSpeed'])
        forecast_wind_direction = forecast['WindDirectionAbreviated']
        forecast_rain = forecast['PrecipitationProbability']

        existing = Forecast.objects.filter(date=forecast_date)
        if existing:
            existing.delete()
        new_forecast = Forecast.objects.create(
            date=forecast_date,
            min_temp = forecast_min_temp,
            max_temp = forecast_max_temp,
            wind_speed = forecast_wind_speed,
            wind_direction = forecast_wind_direction,
            rain = forecast_rain
        )