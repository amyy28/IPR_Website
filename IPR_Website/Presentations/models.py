from django.db import models
from django.urls import reverse
from Teams.models import Teams

# Create your models here.

class Presentations(models.Model):
    team_group_numbers = models.ForeignKey(Teams, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    file = models.FileField(blank=True)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('presentations-detail', kwargs={'pk': self.pk})

