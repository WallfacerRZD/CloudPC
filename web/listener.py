# coding=utf-8

# 解决命令行找不到包
import sys
from json import loads

sys.path.append("F:\python\demo\CloudPC")

from flask import Flask, send_file, request, render_template, Response
from utils.camera import Camera
from utils.manager import Manager

app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    password = request.form["password"]
    if password == "password":
        return "<p>sdf</p>"
    else:
        return u"<p>密码错误了哦</p>"


@app.route("/", methods=["POST", "GET"])
def live():
    return render_template("index.html")


@app.route("/feed_video", methods=["GET"])
def feed_video():
    try:
        return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception:
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
    img_stream = Camera.get_position()
    print 'test'
    return Response(img_stream, mimetype='image/png')


@app.route("/shot_camera", methods=["GET"])
def shot_camera():
    img_stream = Camera.shot_camera()
    return Response(img_stream, mimetype='image/png')


@app.route('/lock', methods=["POST"])
def lock():
    manager = Manager()
    manager.lock()
    return 'sucess'


@app.route('/shut_down', methods=["POST"])
def shut_down():
    manager = Manager()
    manager.shutdown_after(3)
    return 'success'


@app.route('/execute_cmd', methods=['POST'])
def execute_cmd():
    data = loads(request.form.get('data'))
    cmd = data['cmd']
    output = Manager.execute(cmd)
    return output


def generate_frame():
    cam = Camera.frame()
    while True:
        frame = cam.next()
        yield (b"--frame\r\n"
               b"Content-type: image/jpg\r\n\r\n" +

               frame +
               b"\r\n")


@app.route('/', methods=["GET", "POST"])
def index():
    return send_file("static/home.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2333, threaded=True)
