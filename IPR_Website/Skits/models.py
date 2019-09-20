from django.db import models
from django.urls import reverse

# Create your models here.

class Skits(models.Model):
    team_group_numbers = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('skits-detail', kwargs={'pk': self.pk})