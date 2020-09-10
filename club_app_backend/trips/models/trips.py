"""Trips models."""

# Django
from django.db import models

# utilities
from club_app_backend.utils.models import ClubModel


class Trip(ClubModel):
    """Trip model."""

    passenger = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey('cars.Car', on_delete=models.SET_NULL, null=True)

    departure_location = models.CharField(max_length=255)
    arrival_location = models.CharField(max_length=255)
    distance = models.CharField(max_length=255)
    travel_time = models.CharField(max_length=255)

    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text='Used for disabling the ride or marking it as finished.'
    )

    def __str__(self):
        """Return ride details."""
        return '{_from} to {to} | {day} - {f_time}'.format(
            _from = self.departure_location,
            to = self.arrival_location,
            day=self.created.strftime('%a %d, %b'),
            f_time=self.created.strftime('%I:%M %p'),
        )