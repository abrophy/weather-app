from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index' ),
    url(r'^apiv1/forecasts', views.ForecastList.as_view()),
    url(r'^register', views.UserFormView.as_view(), name='register' ),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]