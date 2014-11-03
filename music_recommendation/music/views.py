from django.shortcuts import render
from django.http import HttpResponse
from music.models import Songs
# Create your views here.

def index(request):
	
	results = Songs.objects.all()
	output = ','.join([i.song_name for i in results])
	return HttpResponse(output)
