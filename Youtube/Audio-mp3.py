# importing packages
from pytube import YouTube
import os
  
# url input from user
yt = YouTube(input("Enter the URL of the video you want to download: \n>> "))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  

# replace destination with the path where you want to save the downloaded file
destination = "E:\HDK\BHAKTCHINTAMANI KATHA"
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")


# ----------->>> For PlayList <<<-------------------
# ----------->> Not done Yet, Under Progress 
# # importing packages
# from pytube import Playlist, YouTube
# import os

# # url input from user
# pl = Playlist(input("Enter the URL of the playlist you want to download: \n>> "))

# # get list of video URLs in the playlist
# pl.video_urls

# # show available resolutions for the first video in the playlist
# yt = YouTube(pl.video_urls[0])
# print("Available Resolutions:")
# for stream in yt.streams:
#     if "video/mp4" in str(stream.mime_type):
#         print(stream.resolution)

# # user input for resolution selection
# res = input("Enter the resolution you want to download (e.g. 720p): \n>> ")

# # iterate through videos in playlist
# for i, url in enumerate(pl.video_urls):
#     video = YouTube(url)
#     print(f"Downloading video {i+1} of {len(pl.video_urls)}: {video.title}")
    
#     # filter for selected resolution
#     video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

  
#     # replace destination with the path where you want to save the downloaded file
#     destination = "E:\VS_CODE\Youtube"
  
#     # download the file
#     out_file = video.download(output_path=destination)
  
#     # save the file
#     base, ext = os.path.splitext(out_file)
#     new_file = base + '.mp4'
#     os.rename(out_file, new_file)
  
#     # result of success
    # print(video.title + " has been successfully downloaded in " + res + " resolution.")
