from pyhocon import HOCONConverter, ConfigFactory


def format_hocon(value):
    """"
    This convert a dict to hocon(STR) type.
    """
    config = ConfigFactory().from_dict(value)
    return HOCONConverter.convert(config, 'hocon')


def save_hocon(confist):
    """"
    This function expect a dict with settings and it will write these settings in settings.conf after
    converting it to hocon(STR) using fromat_hocon() above.
    """
    settings = format_hocon(confist)
    f = open("settings.conf", "w+")
    f.write(settings)
    f.close()


def listactions(conf):
    k = [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]
    signs = ['stop', 'point1', 'point2', 'fist', 'grab']
    states = ['aborted', 'playing', 'paused']
    for i in range(0, 5):
        for x in range(0, 3):
            k[i][x] = conf[states[x]][signs[i]]
    return k
