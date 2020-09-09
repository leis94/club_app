"""Cars model"""

# Django
from django.db import models

#Utilities
from club_app_backend.utils.models import ClubModel


class Car(ClubModel):
    """ Cars model.
    
    This model is to create a cars who will takes the trip when a user ordered
    """
    driver = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    license = models.CharField('License car', max_length=10)

    manufactured  = models.CharField('Manufactured car', max_length= 20)
    brand_type = models.CharField('Brand type car', max_length= 20, null=True, blank=True)

    model_year = models.PositiveIntegerField(default=2020)
    color = models.CharField('Color car', max_length=10, null=True, blank=True)

    seats = models.PositiveIntegerField(default=4)

    is_available = models.BooleanField(
        'Available',
        default=True,
        help_text="Car is avaiable when it does not take a trip'"
    )

    is_active = models.BooleanField(
        'Available',
        default=True,
        help_text="Bolean field to set if a car is active or not'"
    )

    def __str__(self):
        """Return car license."""
        return self.license


    def get_driver_name(self):
        "Return driver name"
        return self.driver.first_name





