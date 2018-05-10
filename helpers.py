from functools import wraps
from flask import session
from app import *
from pyhocon import HOCONConverter, ConfigFactory


def format_hocon(value):
    """"
    This convert a dict to hocon(STR) type.
    """
    config = ConfigFactory().from_dict(value)
    return HOCONConverter.convert(config, 'hocon')


def updates():
    conf = ConfigFactory.parse_file(session['path'])
    session['confist'] = dict(conf)


def save_hocon(confist, path):
    """"
    This function expect a dict with settings and it will write these settings in settings.conf after
    converting it to hocon(STR) using fromat_hocon() above.
    """
    settings = format_hocon(confist)
    f = open(path, "w+")
    f.write(settings)
    f.close()


def listactions(conf):
    k = [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]
    signs = ['stop', 'point1', 'point2', 'fist', 'grab']
    states = ['aborted', 'playing', 'paused']
    for i in range(0, 5):
        for x in range(0, 3):
            c = conf[states[x]][signs[i]]
            k[i][x] = c.replace(c[:20], '')
    return k


def path_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.11/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("path") is None:
            return redirect(url_for("display", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def hocon_checker(conf):
    actions = session['confist']['actions']
    signs = ['stop', 'point1', 'point2', 'fist', 'grab']
    states = ['aborted', 'playing', 'paused']
    for i in range(0, 5):
        for x in range(0, 3):
            c = conf[states[x]][signs[i]]
            if c not in actions:
                return False
    return True


def remove_id():
    session['id'] = ''
