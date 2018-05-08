from flask import Flask, render_template, request, redirect, url_for
from helpers import *
from pyhocon import ConfigFactory

app = Flask(__name__)

# Get settings and converting it to dict
conf = ConfigFactory.parse_file('settings.conf')
confist = dict(conf)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        confsec = listactions(confist)
        return render_template('index.html', confist=confsec)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    states = ['aborted', 'playing', 'paused']
    sings = ['stop', 'point1', 'point2', 'fist', 'grab']
    for x in range(0, 3):
        confist[states[x]][sings[id]] = request.form["action" + str(x) + str(id)]
    save_hocon(confist)
    return redirect(url_for("hello_world"))


if __name__ == '__main__':
    app.run()
