# coding=utf-8

# 解决命令行找不到包
import sys
import os

current_path = os.path.abspath('.')
sys.path.append(current_path)

from json import loads, load, dump
from flask import Flask, send_file, request, Response, session, redirect, url_for
from utils.camera import Camera
from utils.manager import Manager
from utils import sender
from subprocess import Popen, PIPE
import socket

app = Flask(__name__)
app.secret_key = 'salkf12323!#!@#$!%fa!@#!4sdzGF'

config = {}
with open('config.json', 'r') as f:
    config = load(f)
user = config['user']
password = config['password']


def has_login():
    return session.get('status') is not None


@app.route("/login", methods=["POST"])
def login():
    if request.form.get('key', '') == config['key']:
        session['status'] = True
    return redirect(url_for('index'))


@app.route("/", methods=["POST", "GET"])
def index():
    if has_login():
        return send_file("static/index.html")
    else:
        return send_file('static/login.html')


@app.route("/feed_video", methods=["GET"])
def feed_video():
    if has_login():
        return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/shot_screen', methods=['GET'])
def shot_screen():
    if has_login():
        img_stream = Camera.shot_screen()
        return Response(img_stream, mimetype='image/png')


@app.route("/position", methods=["GET", "POST"])
def position():
    return send_file('./static/position.html')


@app.route("/get_position", methods=["GET", "POST"])
def get_position():
    if has_login():
        img_stream = Camera.get_position()
        print 'test'
        return Response(img_stream, mimetype='image/png')


@app.route("/shot_camera", methods=["GET"])
def shot_camera():
    if has_login():
        img_stream = Camera.shot_camera()
        return Response(img_stream, mimetype='image/png')


@app.route('/lock', methods=["POST"])
def lock():
    if has_login():
        manager = Manager()
        manager.lock()
        return 'sucess'


@app.route('/shut_down', methods=["POST"])
def shut_down():
    if has_login():
        manager = Manager()
        manager.shutdown_after(3)
        return 'success'


@app.route('/execute_cmd', methods=['POST'])
def execute_cmd():
    if has_login():
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
        # mail_sender = sender.Sender(user, password)
        # mail_sender.send_text('CloudPC', 'CloudPC正在运行,请访问:\n%s:2333' % myaddr, 'plain')
        # 启动
        app.run(host='0.0.0.0', port=2333, threaded=True)
    except Exception, e:
        print '程序启动失败, 请检查配置文件'
        print e
        exit()
