import os
from flask import Flask, render_template, request, redirect, url_for, session
from pyhocon import ConfigFactory
from helpers import *

app = Flask(__name__)
app.secret_key = "K8jf4dl3jqM"


@app.route('/', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        extension = os.path.splitext(request.form['setting'])[1]
        if not os.path.exists(request.form['setting']) or not extension == '.conf':
            return render_template('display.html', error=1)
        else:
            session['path'] = request.form['setting']
            updates()
        remove_id()
        return redirect(url_for('home'))
    else:
        return render_template('display.html')


@app.route('/home', methods=['GET'])
@path_required
def home():
    confsec = listactions(session['confist'])
    return render_template('index.html', confist=confsec)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    conf = session['confist']
    states = ['aborted', 'playing', 'paused']
    sings = [conf['gestures'][0], conf['gestures'][1], conf['gestures'][2], conf['gestures'][3], conf['gestures'][4]]
    for x in range(0, 3):
        session['confist'][states[x]][sings[id]] = session['confist']['actions'][0][:20] + request.form["action" + str(x) + str(id)]
    if hocon_checker(session['confist']):
        save_hocon(session['confist'], session['path'])
    updates()
    session['id'] = id
    return redirect(url_for("home"))


@app.route('/set_option', methods=['POST'])
def set_option():
    remove_id()
    return 'Yes'


if __name__ == '__main__':
    app.run()
