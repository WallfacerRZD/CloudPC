# coding=utf-8

# 解决命令行找不到包
import sys
import os

current_path = os.path.abspath('.')
sys.path.append(current_path)

from json import loads, load, dump
from flask import Flask, send_file, request, render_template, Response
from utils.camera import Camera
from utils.manager import Manager
from utils import sender
from subprocess import Popen, PIPE
import socket
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def live():
    return render_template("index.html")


@app.route("/feed_video", methods=["GET"])
def feed_video():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


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
    not_connected = 1
    # ping百度, 判断是否联网
    while True:
        p = Popen('ping baidu.com', shell=True, stdout=PIPE, stderr=PIPE)
        p.communicate()
        not_connected = p.returncode
        if not not_connected:
            break


    # 获取ip
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)

    # 发送邮件
    try:
        config = {}
        with open('config.json', 'r') as f:
            config = load(f)
        user = config['user']
        password = config['password']
        mail_sender = sender.Sender(user, password)
        mail_sender.send_text('CloudPC', 'CloudPC正在运行,请访问:\n%s:2333' % myaddr, 'plain')
        # 启动
        app.run(host='0.0.0.0', port=2333, threaded=True)
    except Exception, e:
        print '程序启动失败, 请检查配置文件'
        print e
        exit()
