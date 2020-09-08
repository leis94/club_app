"""Profile Model."""

#Django
from django.db import models

#Utilities
from club_app_backend.utils.models import ClubModel

class Profile(ClubModel):
    """Profile model.

    A profile holds a user's public data like biography, picture,
    and statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to = 'users/pictures/',
        blank=True,
        null=True,
    )

    biography = models.TextField(max_length=500, blank=True)

    # Stats
    trips_taken = models.PositiveIntegerField(default=0)

    ranking = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the trips  taken and offered."
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)