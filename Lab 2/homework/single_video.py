# Sample 1: Download a single youtube video
from youtube_dl import YoutubeDL
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4']) # Remember to put your video in a list, eventhough one video is downloaded