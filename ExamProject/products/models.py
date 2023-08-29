from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg

UserModel = get_user_model()


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    NAME_MIN_LEN = 5
    NAME_MAX_LEN = 30

    BRAND_MIN_LEN = 5
    BRAND_MAX_LEN = 30

    DESCRIPTION_MAX_LEN = 300

    QUANTITY_MAX_LEN = 20

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
        ),
        unique=True,
        blank=False,
    )
    brand = models.CharField(
        max_length=BRAND_MAX_LEN,
        validators=(
            MinLengthValidator(BRAND_MIN_LEN),
        ),
        null=False,
        blank=False
    )

    category = models.ManyToManyField(ProductCategory)

    quantity = models.CharField(
        default=' ',
        max_length=QUANTITY_MAX_LEN,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='products/',
        null=False,
        blank=False
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )

    @property
    def full_name(self):
        if self.brand or self.name:
            return f'{self.brand} {self.name}'
        return None

    def average_rating(self) -> float:
        return Rating.objects.filter(product=self).aggregate(Avg("score"))["score__avg"] or 0


class Rating(models.Model):
    MAX_SCORE = 5

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,  # ???
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    score = models.IntegerField(
        default=0,
        validators=(
            MaxValueValidator(MAX_SCORE),
        )
    )

    def __str__(self):
        return str(self.pk)


class Cart(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

