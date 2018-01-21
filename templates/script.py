import os
from flask import Flask, send_file, make_response


APP = Flask(__name__)
MEDIA_PATH = 'C:\Users\Ravi Kishore\Desktop\ML\preloader_with_CSS\hackdemo\Sample Preloaders\Stockbg.mp4'


@APP.route('/<vid_name>')
def serve_video(vid_name):
    vid_path = os.path.join(MEDIA_PATH, vid_name)
    resp = make_response(send_file(vid_path, 'Stockbg/mp4'))
    resp.headers['Content-Disposition'] = 'inline'
    return resp


if __name__ == '__main__':
    APP.run()