# coding=utf-8
from flask import Flask, send_file, redirect, url_for, request

app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    password = request.form["password"]
    if password == "password":
        return "<p>sdf</p>"
    else:
        return u"<p>密码错误了哦</p>"


@app.route("/live", methods=["POST", "GET"])
def live():
    return send_file("static/test.jpg")


@app.route('/', methods=["GET", "POST"])
def index():
    return send_file("static/home.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=2334, debug=True)
