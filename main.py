# importing the module
from pytube import YouTube

link="https://youtu.be/9bZkp7q19f0"

yt = YouTube(link)

# for getting video name
yt.title

# for getting thumbnail url
yt.thumbnail_url

yt.streams.first().download(output_path="videos/")
