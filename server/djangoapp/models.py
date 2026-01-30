from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"

    CAR_TYPE_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
