from django.db import models

# Create your models here.

class Songs(models.Model):
	def __str__(self): 
		return self.song_name
	song_name = models.CharField(max_length=100)
	artist = models.CharField(max_length=100)
	album = models.CharField(max_length=100)	 	
	duration = models.FloatField(default=0)
	rating  = models.IntegerField(default=2)
	genre = models.CharField(max_length=50)
