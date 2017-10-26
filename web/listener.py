# coding=utf-8

# 解决命令行找不到包
import sys
sys.path.append("F:\python\demo\email_receiver")


from flask import Flask, send_file, request, render_template, Response

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
@app.route("/live", methods=["POST", "GET"])
def live():
    return render_template("live.html")


@app.route("/feed_video", methods=["GET"])
def feed_video():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_frame():
    while True:
        frame = Camera.frame().next()
        yield (b"--frame\r\n" +
               b"Content-type: image/jpg\r\n\r\n" +
               frame +
               b"\r\n")


@app.route('/', methods=["GET", "POST"])
def index():
    return send_file("static/home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2334)
