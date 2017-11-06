# coding=utf-8

# 解决命令行找不到包
import sys

sys.path.append("F:\python\demo\email_receiver")

from flask import Flask, send_file, request, render_template, Response, url_for

from utils.camera import Camera

app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    password = request.form["password"]
    if password == "password":
        return "<p>sdf</p>"
    else:
        return u"<p>密码错误了哦</p>"


# 实时监控摄像头
@app.route("/", methods=["POST", "GET"])
def live():
    return render_template("index.html")


@app.route("/feed_video", methods=["GET"])
def feed_video():
    try:
        return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')
    except:
        return ''


@app.route('/shot_screen', methods=['GET'])
def shot_screen():
    img_stream = Camera.shot_screen()
    return Response(img_stream, mimetype='image/png')


@app.route("/position", methods=["GET", "POST"])
def position():
    return send_file('./static/position.html')


@app.route("/get_position", methods=["GET", "POST"])
def get_position():
    print 'tesy'
    img_stream = Camera.get_position()
    return Response(img_stream, mimetype='image/png')


@app.route("/shot_camera", methods=["GET"])
def shot_camera():
    img_stream = Camera.shot_camera()
    return Response(img_stream, mimetype='image/png')


def generate_frame():
    cam = Camera.frame()
    try:
        while True:
            frame = cam.next()
            yield (b"--frame\r\n" +
                   b"Content-type: image/jpg\r\n\r\n" +
                   frame +
                   b"\r\n")
    except Exception, e:
        print e


@app.route('/', methods=["GET", "POST"])
def index():
    return send_file("static/home.html")


if __name__ == "__main__":
    app.run(port=2333, debug=True)
