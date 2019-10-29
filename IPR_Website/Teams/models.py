from django.db import models
from django.urls import reverse
# Create your models here.

class Teams(models.Model):
    team_number = models.IntegerField()
    member_1 = models.CharField(max_length=100)
    member_2 = models.CharField(max_length=100, blank=True)
    member_3 = models.CharField(max_length=100, blank=True)

    def __int__(self):
        return self.team_number

    def get_absolute_url(self):
        return reverse('teams-detail', kwargs={'pk': self.pk})
