from flask import Flask, render_template, request, jsonify
from pytube import YouTube

app = Flask(__name__)

def download_video(video_link, download_type):
    video_url = YouTube(video_link)

    if download_type == 'video':
        video = video_url.streams.get_highest_resolution()
    elif download_type == 'audio':
        video = video_url.streams.filter(only_audio=True).first()
    else:
        return {'error': 'Escolha inválida. Por favor, escolha entre "video" e "audio".'}

    download_link = video.url
    return {'download_link': download_link}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_download', methods=['POST'])
def video_download():
    video_link = request.form['video_url']
    download_type = request.form['download_type']

    result = download_video(video_link, download_type)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
