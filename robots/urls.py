from django.urls import path

from robots.views import get_report

app_name = "robots"

urlpatterns = [
    path('week-report/', get_report)
]
