from django.db import models
from django.urls import reverse
# Create your models here.
class team(models.Model):
    team_group_number = models.IntegerField()
    team_member_1=models.CharField(max_length=100)
    team_member_2 = models.CharField(max_length=100)
    team_member_3 = models.CharField(max_length=100)
    team_usn_1 = models.CharField(max_length=100)
    team_usn_2 = models.CharField(max_length=100)
    team_usn_3 = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('save-team', kwargs={'pk': self.pk})
