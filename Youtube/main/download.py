from flask import Flask, request, send_file
from video_downloader import download_video
import os

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>YouTube Video Downloader</title>
                <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                <script src="script.js"></script>
            </head>
            <body>
                <h1>YouTube Video Downloader</h1>
                <p>Enter the URL of the YouTube video you want to download:</p>
                <input type="text" id="url_input">
                <button id="download_button">Download</button>
                <p id="status_message"></p>
                <a id="download_link" href=""></a>
            </body>
        </html>
    '''


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        download_video(url)
        file_name = url.split('=')[1] + '.mp4'
        return send_file(file_name, as_attachment=True)
    except:
        return 'Error downloading video.'


if __name__ == '__main__':
    app.run()
