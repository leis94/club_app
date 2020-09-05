"""Users model"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from club_app.utils.models import ClubModel

class User(ClubModel, AbstractUser):
    """Users model.

    Extend from Django's Abstract User, change the username field to login by email.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Clients are the main type of users.'
        )
    )

    is_driver = models.BooleanField(
        'driver',
        default=False,
        help_text ='Set to true when the user is a driver'
    )

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']


    def __str__(self):
        """Return Username"""
        return self.username

    def get_short_name(self):
        """Return first_name"""
        return self.first_name