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
@app.route("/live", methods=["POST", "GET"])
def live():
    return render_template("carousel.html")


@app.route("/feed_video", methods=["GET"])
def feed_video():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/position", methods=["GET", "POST"])
def position():
    return send_file('./static/position.html')

@app.route("/get_position", methods=["GET", "POST"])
def get_position():
    return render_template('get_position.html')



def generate_frame():
    cam = Camera()
    try:
        while True:
            frame = cam.frame().next()
            yield (b"--frame\r\n" +
                   b"Content-type: image/jpg\r\n\r\n" +
                   frame +
                   b"\r\n")
    except Exception, e:
        print e
        cam.release_cam()


@app.route('/', methods=["GET", "POST"])
def index():
    return send_file("static/home.html")


# ----------------图片------------------
# @app.route('/static/manager.png', methods=['GET', 'POST'])
# def manager():
#     return Response(file('./static/manager.png'), mimetype='image/png')
#
#
# @app.route('/static/task.png', methods=['GET', 'POST'])
# def task():
#     return Response(file('./static/manager.png'), mimetype='image/png')
#
#
# @app.route('/static/cmd.png', methods=['GET', 'POST'])
# def cmd():
#     return Response(file('./static/cmd.png'), mimetype='image/png')
#
#
# @app.route('/static/camera.png', methods=['GET', 'POST'])
# def camera():
#     return Response(file('./static/camera.png'), mimetype='image/png')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=2333)
