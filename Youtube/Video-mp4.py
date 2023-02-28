# # importing packages
# from pytube import YouTube
# import os
  
# # url input from user
# yt = YouTube(input("Enter the URL of the video you want to download: \n>> "))
  
# # show available streams (resolutions)
# print("Available Resolutions:")
# for stream in yt.streams:
#     if "video/mp4" in str(stream.mime_type):
#         print(stream.resolution)

# # user input for resolution selection
# res = input("Enter the resolution you want to download (e.g. 720p): \n>> ")

# # filter for selected resolution
# video = yt.streams.filter(res=res, mime_type="video/mp4").first()
  
# # replace destination with the path where you want to save the downloaded file
# destination = "E:\VS_CODE\Youtube"
  
# # download the file
# out_file = video.download(output_path=destination)
  
# # save the file
# base, ext = os.path.splitext(out_file)
# new_file = base + '.mp4'
# os.rename(out_file, new_file)
  
# # result of success
# print(yt.title + " has been successfully downloaded in " + res + " resolution.")


# importing packages
from pytube import YouTube
from moviepy.editor import *
import os

# url input from user
yt = YouTube(input("Enter the URL of the video you want to download: \n>> "))

# show available streams (resolutions)
print("Available Resolutions:")
for stream in yt.streams:
    if "video/mp4" in str(stream.mime_type):
        print(stream.resolution)

# user input for resolution selection
res = input("Enter the resolution you want to download (e.g. 720p): \n>> ")

# filter for selected resolution
video = yt.streams.filter(res=res, mime_type="video/mp4").first()

# get audio stream
audio = yt.streams.filter(only_audio=True).first()

# replace destination with the path where you want to save the downloaded file
destination = "E:\VS_CODE\Youtube"

# download the files
video_out_file = video.download(output_path=destination)
audio_out_file = audio.download(output_path=destination)

# merge audio and video
video_clip = VideoFileClip(video_out_file)
audio_clip = AudioFileClip(audio_out_file)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(base + '.mp4')

# remove intermediate files
os.remove(video_out_file)
os.remove(audio_out_file)

# result of success
print(yt.title + " has been successfully downloaded in " + res + " resolution with audio.")
