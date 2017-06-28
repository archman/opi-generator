from opimodel import utils
import sys


class Color(object):
    """Representation of a color."""

    def __init__(self, rgb=(0, 0, 0),  name=None):
        self.red, self.green, self.blue = rgb
        self.name = name


def parse_css_color_file(filepath):
    """Parse the provided color.def file, create Color objects for each
       defined color and attach them to the namespace of this module wth
       names converted into appropriate constants by the
       utils.mangle_name() function.

    Args:
        filepath of the color file
    """
    with open(filepath) as f:
        for line in (l.strip() for l in f.readlines()):
            if not line == '' and not line.startswith('#'):
                key, value = [x.strip() for x in line.split('=')]
                r, g, b = [int(x.strip(',')) for x in value.split()]
                utils.add_attr_to_module(key, Color((r, g, b), key),
                                  sys.modules[__name__])
