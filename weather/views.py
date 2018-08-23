from django.views import generic
from .models import Forecast

app_name = 'weather'

class IndexView(generic.ListView):
    template_name = 'weather/index.html'
    context_object_name = 'forecasts'

    def get_queryset(self):
        return Forecast.objects.all()