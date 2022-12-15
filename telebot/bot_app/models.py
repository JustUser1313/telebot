from django.db import models


class UserProfile(models.Model):

    user_id = models.PositiveIntegerField(
        verbose_name="User Telegram ID",
        unique=True
    )
    user_city = models.TextField(
        verbose_name="city that user have entered"
    )
    first_name = models.TextField(
        verbose_name="User first_name"
    )
    last_name = models.TextField(
        verbose_name="User last_name"
    )

    class Meta:
        verbose_name = "User Profile"
