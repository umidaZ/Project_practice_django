from django.shortcuts import render
# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def stopWatch(request):
    return render(request, 'stopwatch.html')

def clock(request):
    return render(request, 'clock.html')