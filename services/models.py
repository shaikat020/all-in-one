from django.db import models
from django.contrib.auth.models import User

# 1) Cafeteria Menu & Meal Schedules
class CafeteriaMenu(models.Model):
    day = models.DateField()
    meal_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Optional: to simulate pre-ordering
    # You could link a user to a pre-order, but for simplicity:
    # is_preorder_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day} - {self.meal_name}"

# 2) University Bus Routes & Schedules
class BusRoute(models.Model):
    route_name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)

    def __str__(self):
        return self.route_name

class BusSchedule(models.Model):
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    # You can add fields for notifications, delays, etc.

    def __str__(self):
        return f"{self.route.route_name} - {self.departure_time} to {self.arrival_time}"

# 3) Class Schedules & Faculty Contacts
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.course_name

class ClassSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # e.g., "Monday"
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_name} on {self.day_of_week}"

# 4) Event & Club Management
class Club(models.Model):
    club_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.club_name

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.event_name

# 5) (Optional) Campus Navigation - just a placeholder
class CampusBuilding(models.Model):
    building_name = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.building_name
