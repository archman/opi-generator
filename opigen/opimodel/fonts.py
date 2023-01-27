from . import utils
import sys


REGULAR = 0
BOLD = 1
ITALIC = 2
BOLD_ITALIC = 3


STYLES = {'regular': REGULAR,
          'bold': BOLD,
          'italic': ITALIC,
          'bold italic': BOLD_ITALIC}

# notes for Phoebus:
# - Only supports font size in pixels
# - String as font style

# phoebus font style
STYLE_MAP = {
    REGULAR: 'REGULAR',
    BOLD: 'BOLD',
    ITALIC: 'ITALIC',
    BOLD_ITALIC: 'BOLD_ITALIC',
}


class Font(object):
    """Representation of a font."""

    def __init__(self, name=None, fontface='Liberation Sans',
            size=15, style=REGULAR, pixels=True):
        # If the font name is specified, and defined in CS-Studio's fonts.def
        # than this overrides all over attributes.
        self.fontface = fontface
        self.size = size
        self.style = style
        self.pixels = pixels
        self.name = name

    def __eq__(self, other):
        val = (self.size == other.size and
               self.style == other.style and
               self.pixels == other.pixels)
        return val
    
    def style_as_str(self) -> str:
        # phoebus font style
        return STYLE_MAP[self.style]

    def __str__(self):
        pixels_or_points = 'px' if self.pixels else 'pt'
        format_string = 'Font name {}: {} style {} size {}{}'
        return format_string.format(self.name, self.fontface, self.style,
                                    self.size, pixels_or_points)


def parse_css_font_file(filename):
    """Parse the provided font.def file, create Font objects for each
       defined font and attach them to the namespace of this module wth
       names converted into appropriate constants by the
       utils.mangle_name() function.

    Args:
        filepath of the font file
    """
    with open(filename) as f:
        for line in (l.strip() for l in f.readlines()):
            if line and not line.startswith('#'):
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
                    pixels = False
                style_int = STYLES[style]
                f = Font(key, face, size, style_int, pixels)
                utils.add_attr_to_module(key, f, sys.modules[__name__])
