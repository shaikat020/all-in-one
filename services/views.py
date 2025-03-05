from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import date

from .models import (
    CafeteriaMenu, 
    BusRoute, 
    BusSchedule,
    Faculty, 
    Course, 
    ClassSchedule, 
    Club, 
    Event,
    CampusBuilding
)

def index(request):
    return render(request, 'index.html')

# ---------------------
# Authentication Views
# ---------------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

# ---------------------
# 1) Cafeteria Menus
# ---------------------
def cafeteria_view(request):
    today = date.today()
    menus = CafeteriaMenu.objects.filter(day=today)
    context = {
        'menus': menus,
        'today': today
    }
    return render(request, 'cafeteria.html', context)

# ---------------------
# 2) Bus Routes & Schedules
# ---------------------
def bus_schedules_view(request):
    routes = BusRoute.objects.all()
    schedules = BusSchedule.objects.all()
    context = {
        'routes': routes,
        'schedules': schedules
    }
    return render(request, 'bus_schedules.html', context)

# ---------------------
# 3) Class Schedules & Faculty Contacts
# ---------------------
@login_required
def class_schedules_view(request):
    # If you want to fetch class schedules for the currently logged in user, 
    # you'd create a relationship with User. For simplicity, show all:
    schedules = ClassSchedule.objects.all()
    faculty = Faculty.objects.all()
    courses = Course.objects.all()
    context = {
        'schedules': schedules,
        'faculty': faculty,
        'courses': courses
    }
    return render(request, 'class_schedules.html', context)

# ---------------------
# 4) Events & Clubs
# ---------------------
def events_view(request):
    clubs = Club.objects.all()
    events = Event.objects.all().order_by('event_date')
    context = {
        'clubs': clubs,
        'events': events
    }
    return render(request, 'events.html', context)

# ---------------------
# 5) (Optional) Campus Navigation 
# ---------------------
def campus_map_view(request):
    buildings = CampusBuilding.objects.all()
    context = {
        'buildings': buildings
    }
    return render(request, 'campus_map.html', context)

# Example JSON endpoint if you need data for an AR or interactive map
def buildings_json(request):
    buildings_data = list(CampusBuilding.objects.all().values())
    return JsonResponse(buildings_data, safe=False)
