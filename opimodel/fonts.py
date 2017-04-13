REGULAR = 0
BOLD = 1
ITALIC = 2
BOLD_ITALIC = 3


STYLES = {'regular': REGULAR,
          'bold': BOLD,
          'italic': ITALIC,
          'bold italic': BOLD_ITALIC}


class Font(object):

    def __init__(self, fontface, size, style=REGULAR, name=None, pixels=True):
        self.fontface = fontface
        self.size = size
        self.style = style
        self.pixels = pixels


def parse_font_file(filename):
    def_fonts = {}
    with open(filename) as f:
        for line in (l.strip() for l in f.readlines()):
            if not line == '' and not line.startswith('#'):
                key, value = [x.strip() for x in line.split('=')]
                face, style, size = [x.strip(',') for x in value.split('-')]
                pixels = True
                if size.endswith('px'):
                    size = int(size[:-2])
                elif size.endswith('pt'):
                    size = int(size[:-2])
                    pixels = False
                else:
                    size = int(size)
                style_int = STYLES[style]
                def_fonts[key] = Font(face, size, style_int, pixels=pixels)
    return def_fonts
