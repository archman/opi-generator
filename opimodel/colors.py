class Color(object):

    def __init__(self, r, b, g, name=None):
        self.red = r
        self.blue = b
        self.green = g
        self.name = name


GREY_2 = Color(219, 219, 219, 'grey-2')
GREY_8 = Color(134, 134, 134, 'grey-8')
BLACK = Color(0, 0, 0, 'black')
TOP_SHADOW = Color(237, 237, 237, 'Top Shadow')
BUTTON_ON = Color(188, 188, 188, 'Button: On')
