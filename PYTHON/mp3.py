import pytube
from moviepy.editor import *
import os

# Enter the URL of the YouTube playlist
playlist_url = "https://www.youtube.com/playlist?list=PLxCzCOWd7aiG58-6ris4Wa9OjEDfyvkNZ"

# Enter the destination folder for the downloaded files
destination = r"E:\test"

# Create a YouTube object for the playlist
playlist = pytube.Playlist(playlist_url)

# Iterate through the videos in the playlist and download them in .mp4 format
for video in playlist.videos:
    try:
        video.streams.filter(only_audio=True).first().download(output_path=destination)
        video_title = video.title
        print(f"{video_title}.mp4 downloaded")

        # Convert the .mp4 file to .mp3 format
        video_clip = AudioFileClip(os.path.join(destination, f"{video_title}.mp4"))
        video_clip.write_audiofile(os.path.join(destination, f"{video_title}.mp3"))
        video_clip.close()

        # Delete the original .mp4 file
        os.remove(os.path.join(destination, f"{video_title}.mp4"))

        # Show a message indicating that the .mp3 file has been downloaded
        print(f"{video_title}.mp3 downloaded")
    except Exception as e:
        print(f"Error downloading {video.title}: {e}")
