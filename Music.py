import time
import re
import thread

from mutagen.mp3 import MP3
from pyechonest import config
from mutagen.easyid3 import EasyID3
from pyechonest import track
from os import walk

musicPath="/home/karma/Music/"
count=0

def songDetails (songName):
  global count
  print songName
  if re.search('\.[mM][pP]3$',songName):    #Checking if the file is a mp3 file or not
    startTime=time.time()
    f = open(musicPath+songName)
    t = track.track_from_file(f, 'mp3',30,False)
    endTime=time.time();
    print songName
    print t.id
    print t.artist
    print t.duration
    print t.title
    print "Search Time : "+str(endTime-startTime)
    print "----------------------"
    fo = open("foo.txt", "a")
    fo.write( songName+"\n")
    fo.write( t.title+"\n")
    fo.write( t.artist+"\n")
    fo.write( "------------\n")
    # Close opend file
    fo.close()
  count+=1


config.ECHO_NEST_API_KEY="YPRX3VC0QWHMEEJZJ"

#listing all the files in a directory
l = []

for (dirpath, dirnames, filenames) in walk(musicPath):
    	l.extend(filenames)
	break
musicCount=len(l)
print "Number of file : "+str(musicCount)
print "----------------------"

#listing details of the tags

from mutagen.mp3 import MP3
'''
for index in range(musicCount):
  try:
    thread.start_new_thread(songDetails,(l[index],))
  except:
    print "Error: unable to start thread"
'''
#Editing the Tags of the songs

for index in range(musicCount):
  if re.search('\.[mM][pP]3$',l[index]):    #Checking if the file is a mp3 file or not
    audio = MP3(musicPath+l[index],ID3=EasyID3)
    if 'title' in audio:
      print "Title : "+str(audio['title'])
    if 'artist' in audio:
      print "Artist: "+str(audio['artist'])
    if 'album' in audio:
      print "Album : "+str(audio['album'])
    if 'genre' in audio:
      print "Genre : "+str(audio['genre'])
    print "----------------------"

#FIND OUT GENRE OF THE LIST
#FIND OUT ARTIST COUNT
prevCount=0;
while count<100:
  if prevCount != count:
    prevCount=count
    print str(count)
  pass
