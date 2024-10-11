from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import valid_file_size
class Photo(models.Model):

    photo = models.ImageField(
        validators=[
            valid_file_size
        ],
        upload_to='images'
    )

    description = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(10)
        ],
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True
    )






