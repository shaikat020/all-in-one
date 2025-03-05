from django.contrib import admin
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

admin.site.register(CafeteriaMenu)
admin.site.register(BusRoute)
admin.site.register(BusSchedule)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(ClassSchedule)
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(CampusBuilding)
