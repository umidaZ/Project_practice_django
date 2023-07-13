from django.urls import path
from .views import homePage, stopWatch, clock

urlpatterns = [
    path('', homePage, name='home'),
    path('/stopwatch', stopWatch, name='stopwatch'),
    path('/clock', clock, name='clock'),
]