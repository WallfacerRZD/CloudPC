from flask import Flask, send_file, url_for, render_template

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return send_file('static/login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('carousel.html')


@app.route('/img', methods=['GET', 'POST'])
def img():
    return send_file('test.jpeg')


@app.route('/position', methods=['GET', 'POST'])
def position():
    return send_file('static/position.html')


@app.route('/css1', methods=['GET', 'POST'])
def css1():
    return send_file('static/css/bootstrap.css')


@app.route('/css2', methods=['GET', 'POST'])
def css2():
    return send_file('static/css/style.css')


@app.route('/static/manager.png', methods=['GET', 'POST'])
def manager():
    return send_file('static/manager.png')


@app.route('/static/task.png', methods=['GET', 'POST'])
def task():
    return send_file('static/task.png')


@app.route('/static/cmd.png', methods=['GET', 'POST'])
def cmd():
    return send_file('static/cmd.png')


@app.route('/static/camera.png', methods=['GET', 'POST'])
def camera():
    return send_file('static/camera.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2333)
