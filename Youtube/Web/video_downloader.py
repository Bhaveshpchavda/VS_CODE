import pytube


def download_video(url):
    # Create a YouTube object
    youtube = pytube.YouTube(url)

    # Get the first stream with the highest resolution
    video_stream = youtube.streams.filter(
        progressive=True).order_by('resolution').desc().first()

    # Download the video
    video_stream.download()
