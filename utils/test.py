# manage.py
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template, abort

import message


msgsrv = message.MessageServer()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('message.html')


@app.route('/message/')
def message():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        msgsrv.observers.append(ws)
        while True:
            if ws.socket:
                message = ws.receive()
                if message:
                    msgsrv.add_message("%s" % message)
            else:
                abort(404)
    return "Connected!"


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
# message.py
from geventwebsocket import WebSocketError


class MessageServer(object):

    def __init__(self):
        self.observers = []

    def add_message(self, msg):
        for ws in self.observers:
            try:
                ws.send(msg)
            except WebSocketError:
                self.observers.pop(self.observers.index(ws))
                print ws, 'is closed'
                continue
<!-- templates/message.html -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta http-equiv="Content-Language" content="zh-CN"/>
        <title>实时消息</title>
        <link rel="stylesheet" href="http://getbootstrap.com/2.3.2/assets/css/bootstrap.css">
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script type="text/javascript" charset="utf-8">
        $(document).ready(function(){
            $('form').submit(function(event){
                ws.send($(this).serialize());
                return false;
            });
            if ("WebSocket" in window) {
                ws = new WebSocket("ws://" + document.domain + ":5000/message/");
                ws.onmessage = function (msg) {
                    console.log(msg.data);
                };
            } else {
                alert("WebSocket not supported");
            }
            window.onbeforeunload = function() {
                ws.onclose = function () {
                    console.log('unlodad')
                };
                ws.close()
            };
        });
        </script>
    </head>
    <body>
        <div class="header container">
            <h1>实时消息</h1>
            <ul class="tabs">
                <li class="active">
                    <a href="/">DEMO</a>
                </li>
            </ul>
        </div>
        <div class="container">
            Pls check your Chrome console.
            <form class="row" id="message_form">
                <div class="span10">
                    <div class="clearfix">
                        <label for="chat_content">消息</label>
                        <div class="input">
                            <textarea id="chat_content" name="content" class="xlarge" rows="6"></textarea>
                        </div>
                    </div>
                    <div class="well align-center">
                        <input type="submit" class="btn primary" value="发布">
                        &nbsp;
                        <input type="reset" class="btn" value="清空">
                    </div>
                </div>
            </form>
        </div>
        <div class="footer container">
            <p>
                &copy; Copyright by shonenada
            </p>
        </div>
    </body>
</html>
