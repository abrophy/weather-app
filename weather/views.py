from django.views import generic
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Forecast
from .forms import UserForm

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/weather/register/'
    redirect_field_name = 'redirect_to'
    template_name = 'weather/index.html'
    context_object_name = 'forecasts'

    def get_queryset(self):
        return Forecast.objects.all()

class UserFormView(View):
    form_class = UserForm
    template_name = 'weather/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('weather:index')
        
        return render(request, self.template_name, {'form': form})

