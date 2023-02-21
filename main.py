from pytube import YouTube
from sys import argv

link ="link"
vd=YouTube(link)

print("Title: ",vd.title)
print("Views: ",vd.views)
print("Length: ",vd.length)
print("Decription: ",vd.description)
print("Rating: ",vd.rating)

video = vd.streams.first()#choose format
video.download("Choose folder path")