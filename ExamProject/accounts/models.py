from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.templatetags.static import static


def only_letters(value):
    for symbol in value:
        if not symbol.isalpha():
            raise ValidationError('Use only alphabetical letters!')


def only_nums_and_letters(value):
    for symbol in value:
        if not symbol.isalpha() and not symbol.isdigit():
            raise ValidationError('Use only alphabetical letters and numbers!')


def only_nums(value):
    for symbol in value:
        if not symbol.isdigit():
            raise ValidationError('Use only numbers!')


class StoreUser(AbstractUser):
    USERNAME_MIN_LEN = 5
    USERNAME_MAX_LEN = 30

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    ADDRESS_MAX_LEN = 100

    PHONE_NUM_MAX_LEN = 12
    PHONE_NUM_MIN_LEN = 10

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            only_nums_and_letters,
            MinLengthValidator(USERNAME_MIN_LEN),
        ),
        unique=True,
        blank=False,
    )
    email = models.EmailField(
        unique=True,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            only_letters,
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        ),
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            only_letters,
            MinLengthValidator(LAST_NAME_MIN_LEN),
        ),
        null=True,
        blank=True
    )
    delivery_address = models.CharField(
        max_length=ADDRESS_MAX_LEN,
        null=True,
        blank=True
    )
    profile_picture = models.URLField(
        default=static('images/person.png'),
        blank=True,
    )
    phone_number = models.CharField(
        max_length=PHONE_NUM_MAX_LEN,
        validators=(
            only_nums,
            MinLengthValidator(PHONE_NUM_MIN_LEN),
        ),
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
