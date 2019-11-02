from django.db import models
from django.urls import reverse
# Create your models here.

class Teams(models.Model):
    team_number = models.CharField(max_length=100)
    member_1_name = models.CharField(max_length=100)
    member_1_usn = models.CharField(max_length=100)
    member_2_name = models.CharField(max_length=100, blank=True)
    member_2_usn = models.CharField(max_length=100, blank=True)

    member_3_name = models.CharField(max_length=100, blank=True)
    member_3_usn = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.team_number

    def get_absolute_url(self):
        return reverse('teams-detail', kwargs={'pk': self.pk})
