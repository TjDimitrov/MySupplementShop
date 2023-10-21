from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def only_letters(value):
    for symbol in value:
        if not symbol.isalpha():
            raise ValidationError('Use only alphabetical letters!')


class TeamMember(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    DESCRIPTION_MAX_LEN = 100

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            only_letters,
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        ),
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            only_letters,
            MinLengthValidator(LAST_NAME_MIN_LEN),
        ),
        null=False,
        blank=False
    )
    profile_photo = models.ImageField(
        upload_to='team_members/',
        null=False,
        blank=True
    )
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        null=False,
        blank=False
    )
    twitter_socials = models.URLField(
        null=False,
        blank=False
    )
    facebook_socials = models.URLField(
        null=False,
        blank=False
    )
    instagram_socials = models.URLField(
        null=False,
        blank=False
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
