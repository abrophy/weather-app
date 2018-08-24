# WEATHER APPLICATION

This is a django application used to pull and view weather data from the
news24 weather api.

Currently the app is only configured to view daily weather forecasts for
cape town.

# RETRIEVING FORECASTS

there is a custom django management task for retrieving the present
date's weather forecast.

Configure a crontask to perform the action via:

```
python manage.py getweather
```

in the app's directory

# ADMINISTRATION

After installing the app on a server you can create a super user via

```
python manage.py createsuperuser
```

follow the prompts to add a superuser account to the application.

Administration tasks can be performed on users, groups and forecast
records by navigating to the following url:

`<base-url>/admin`

# JSON API

once hosted you can retrieve a list of forecasts in JSON format by
sending basic HTTP auth requests to the following url:

`<base-url>/apiv1/forecasts.json`
