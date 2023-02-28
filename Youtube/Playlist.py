# importing packages
from pytube import Playlist, YouTube
import os

# url input from user
playlist_url = input("Enter the URL of the playlist you want to download: \n>> ")

# optional: create a folder for the playlist
playlist = Playlist(playlist_url)
playlist_title = playlist.title

# optional: create a folder for the playlist
create_folder = input("Do you want to create a folder for the playlist? (y/n): ")
if create_folder.lower() == "y":
    folder_path = os.path.join(os.getcwd(), playlist_title + " playlist")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder created for {playlist_title} playlist.")
else:
    folder_path = os.getcwd()

# loop through all the videos in the playlist
for video in playlist.videos:
    try:
        # extract only audio
        audio = video.streams.filter(only_audio=True).first()

        # optional: check if the file already exists in the folder
        file_path = os.path.join(folder_path, audio.default_filename)
        if os.path.exists(file_path):
            print(f"{audio.default_filename} already exists in the folder. Skipping...")
            continue

        # print the video title
        print(f"Downloading {video.title}...")

        # download the file
        with audio.stream() as stream, open(file_path, "wb") as file:
            # optional: show download progress
            print(f"Size: {round(audio.filesize / (1024*1024), 2)} MB")
            downloaded = 0
            while True:
                buffer = stream.read(4096)
                if not buffer:
                    break
                file.write(buffer)
                downloaded += len(buffer)
                print(f"{round(downloaded/audio.filesize*100)}% downloaded ({round(downloaded/1024)} KB/s)", end="\r")
            print()

        # result of success
        print(f"{video.title} has been successfully downloaded.")
    except Exception as e:
        print(f"Error downloading {video.title}: {e}")
