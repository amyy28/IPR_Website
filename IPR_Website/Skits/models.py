from django.db import models
from django.urls import reverse
from Teams.models import Teams

# Create your models here.

class Skits(models.Model):
    # team_group_numbers = models.CharField(max_length=100)
    team_group_number_1 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name='first')
    team_group_number_2 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name = 'second')
    topic = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('skits-detail', kwargs={'pk': self.pk})
