from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^weather/', include('weather.urls', namespace='weather', app_name='weather')),
]
