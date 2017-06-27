NONE_STYLE = 0
LINE_STYLE = 1


class Border(object):  # pragma pylint: disable=too-few-public-methods

    def __init__(self, style, width, color, alarm):
        self.alarm = alarm
        self.color = color
        self.style = style
        self.width = width
