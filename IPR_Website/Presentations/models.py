from django.db import models
from django.urls import reverse
from Teams.models import Teams

# Create your models here.

class Presentations(models.Model):
    team_group_numbers = models.ForeignKey(Teams, on_delete=models.CASCADE, help_text="Please add your team first if not yet done.")
    topic = models.CharField(max_length=100)
    image_1 = models.FileField(blank=True)
    image_2 = models.FileField(blank=True)
    image_3 = models.FileField(blank=True)
    file = models.FileField(blank=True)
    description = models.TextField(max_length = 1000, help_text="Please don't exceed 450 characters.")

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('presentations-detail', kwargs={'pk': self.pk})

