class Color(object):

    def __init__(self, rgb=(0, 0, 0),  name=None):
        self.red, self.green, self.blue = rgb
        self.name = name


def parse_color_file(filename):
    def_colors = {}
    with open(filename) as f:
        for line in (l.strip() for l in f.readlines()):
            if not line == '' and not line.startswith('#'):
                key, value = [x.strip() for x in line.split('=')]
                r, g, b = [x.strip(',') for x in value.split()]
                def_colors[key] = Color(r, g, b, key)
    return def_colors


BLACK = Color((0, 0, 0), 'Black')
RED = Color((255, 0, 0), 'Red')
GREEN = Color((0, 255, 0), 'Green')
BLUE = Color((0, 0, 255), 'Blue')
