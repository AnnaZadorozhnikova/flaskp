from collections import namedtuple

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


Message = namedtuple('Message', 'text tag')
messages = []

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route("/main", methods=['GET'])
def main():
    return render_template("main.html", messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    messages.append(Message(text,tag))

    return redirect(url_for('main'))


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/stop')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')