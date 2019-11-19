from django.db import models
from django.urls import reverse
# Create your models here.

class Teams(models.Model):
    team_number = models.CharField(max_length=100, help_text="Format: Team 1, Team 2 etc..")
    member_1 = models.CharField(max_length=100)
    member_1_USN = models.CharField(max_length=100)
    member_2 = models.CharField(max_length=100, blank=True)
    member_2_USN = models.CharField(max_length=100, blank=True)

    member_3 = models.CharField(max_length=100, blank=True)
    member_3_USN = models.CharField(max_length=100, blank=True)
    group_photo = models.ImageField(default='default.jpg',upload_to='profile_pics', help_text="Preferrably landscape pictures.")

    def __str__(self):
        return self.team_number

    def get_absolute_url(self):
        return reverse('teams-detail', kwargs={'pk': self.pk})
