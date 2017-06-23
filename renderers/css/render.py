import lxml.etree as et

from renderers.css.actions import OpiAction
from renderers.css.borders import OpiBorder
from renderers.css.colors import OpiColor
from renderers.css.fonts import OpiFont
from renderers.css.rules import OpiRule
from renderers.css.text import OpiText
from renderers.css.widget import OpiWidget


def get_opi_renderer(widget):
    tr = OpiText()
    wr = OpiWidget(tr)

    wr.add_renderer('actions', OpiAction())

    wr.add_renderer('rules', OpiRule())

    cr = OpiColor()
    wr.add_renderer('background_color', cr)
    wr.add_renderer('foreground_color', cr)
    wr.add_renderer('bulb_border_color', cr)
    wr.add_renderer('off_color', cr)
    wr.add_renderer('on_color', cr)
    wr.add_renderer('line_color', cr)

    wr.add_renderer('border', OpiBorder(tr, cr))

    wr.add_renderer('font', OpiFont())
    return OpiRenderer(widget, wr)


class OpiRenderer(object):

    def __init__(self, model, widget_renderer):
        self._model = model
        self._node = None
        self._widget_renderer = widget_renderer

    def assemble(self, model=None, parent=None):
        if model is None:
            model = self._model
        self._node = self._widget_renderer.render(model, parent)

    def get_node(self):
        return self._node

    def __str__(self):
        self.assemble()
        return str(et.tostring(self._node))

    def write_to_file(self, filename):
        self.assemble()
        tree = et.ElementTree(self._node)
        tree.write(filename, pretty_print=True)
