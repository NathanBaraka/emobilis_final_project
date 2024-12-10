from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()  # Maximum occupants
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=255, default="Default Name")  # User's name
    email = models.EmailField(default="default@example.com")
    checkin = models.DateField()
    checkout = models.DateField()
    adult_count = models.PositiveIntegerField()  # Number of adults
    child_count = models.PositiveIntegerField(default=0)  # Number of children
    room_type = models.CharField(max_length=50, default="Room 1")  # Room type (Room 1, Room 2, etc.)
    special_request = models.TextField(blank=True, null=True)  # Optional special request field

    def __str__(self):
        return f"{self.name} - {self.room_type} ({self.checkin} to {self.checkout})"


