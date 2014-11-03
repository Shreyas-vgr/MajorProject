from django.shortcuts import render
from django.http import HttpResponse
from music.models import Songs
from django.template import RequestContext, loader
# Create your views here.

def index(request):
	
	results = Songs.objects.all()
	#template = loader.get_template('music/index.html')
	#output = ','.join([i.song_name for i in results])
	context = { 'results' : results }
	return render(request,'music/index.html',context)
