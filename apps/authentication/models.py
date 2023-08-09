from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICE = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné')
    )

    photo_profil = models.ImageField(verbose_name='Photo de profil')

    role = models.CharField(max_length=63,
                            choices=ROLE_CHOICE,
                            verbose_name='Rôle')
