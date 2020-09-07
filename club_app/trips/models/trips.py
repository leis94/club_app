"""Cars model"""

# Django
from django.db import models

#Utilities
from club_app.utils.models import ClubModel


class Trip(ClubModel):
    "Trip model."""
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    passenger = models.ForeignKey('users.User', related_name='passengers', on_delete=models.CASCADE)

    departure_location = models.CharField(max_length=255)
    departure_date = models.DateTimeField(blank=True, null=True)

    arrival_location = models.CharField(max_length=255)
    arrival_date = models.DateTimeField(blank=True, null=True)

    distance = models.FloatField(null=True)
    travel_time = models.DateTimeField(null=True)

    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text='Used for disabling the ride or marking it as finished.'
    )


    def __str__(self):
        """Return ride details."""
        return '{_from} to {to} | {day} {i_time} - {f_time} | {distance} and time {t_time}|'.format(
            _from = self.departure_location,
            to = self.arrival_location,
            day=self.departure_location.strftime('%a %d, %b'),
            i_time=self.departure_date.strftime('%I:%M %p'),
            f_time=self.arrival_date.strftime('%I:%M %p'),
            distance= self.distance,
            t_time= self.travel_time.strptime("%M:%S")
        )
