#pip install pytube

#import the package
from pytube import YouTube

url = input("Lien de la vidéo : \n")
my_video = YouTube(url)

print("*********************Video Title************************")
#get Video Title
print(my_video.title)

# print("********************Download video*************************")
# #get all the stream resolution for the 
# for stream in my_video.streams:
#     print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#Download video
my_video.download()