from django.urls import path

from robots.views import create_robot

app_name = 'robots'

urlpatterns = [
    path('', create_robot),
]
