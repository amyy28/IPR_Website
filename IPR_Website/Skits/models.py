from django.db import models
from django.urls import reverse
from Teams.models import Teams

# Create your models here.

class Skits(models.Model):
    # team_group_numbers = models.CharField(max_length=100)
    team_group_number_1 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name='first', help_text="Please add your team first if not yet done.")
    team_group_number_2 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name = 'second', help_text="Please add your team first if not yet done.")
    topic = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100, help_text="Please add the embedded url link only.")
    image_1 = models.ImageField(default='default.jpg',upload_to='profile_pics')
    image_2 = models.ImageField(default='default.jpg',upload_to='profile_pics')
    image_3 = models.ImageField(default='default.jpg',upload_to='profile_pics')
    description = models.TextField(max_length = 1000, help_text="Please don't exceed 450 characters.")
    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('skits-detail', kwargs={'pk': self.pk})
