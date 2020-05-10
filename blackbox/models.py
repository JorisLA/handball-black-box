from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Team(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Fine(models.Model):
    name = models.CharField(max_length=200)
    cost = models.PositiveSmallIntegerField(default=0)
    teams = models.ManyToManyField(Team)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class UserFineHistoric(models.Model):
    users = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    total_payment = models.PositiveSmallIntegerField(default=0)
