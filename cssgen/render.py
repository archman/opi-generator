import xml.etree.ElementTree as et
from cssgen import actions, rules, colors, borders, fonts
import collections


def get_opi_renderer(widget):
    tr = OpiTextRenderer()
    wr = OpiWidgetRenderer(tr)
    ar = actions.OpiActionRenderer()
    wr.add_renderer('actions', ar)
    rr = rules.OpiRuleRenderer()
    wr.add_renderer('rules', rr)
    cr = colors.OpiColorRenderer()
    br = borders.OpiBorderRenderer(tr, cr)
    fr = fonts.OpiFontRenderer()
    wr.add_renderer('background_color', cr)
    wr.add_renderer('foreground_color', cr)
    wr.add_renderer('bulb_border_color', cr)
    wr.add_renderer('off_color', cr)
    wr.add_renderer('on_color', cr)
    br = borders.OpiBorderRenderer(tr, cr)
    wr.add_renderer('border', br)
    wr.add_renderer('font', fr)
    return OpiRenderer(widget, wr)


class OpiTextRenderer(object):

    def render(self, widget_node, tag_name, model):
        text_node = et.SubElement(widget_node, tag_name)
        if model is True:
            text_node.text = 'true'
        elif model is False:
            text_node.text = 'false'
        else:
            text_node.text = str(model)


class OpiWidgetRenderer(object):

    def __init__(self, text_renderer):
        self._text_renderer = text_renderer
        self._renderers = collections.defaultdict(lambda: self._text_renderer)

    def add_renderer(self, tag, renderer):
        self._renderers[tag] = renderer

    def render(self, model, parent):
        if parent is None:
            node = et.Element(model._name)
        else:
            node = et.SubElement(parent, model._name)
        node.set('typeId', model._typeId)
        for var, val in sorted(vars(model).items()):
            if not var.startswith('_'):
                self._renderers[var].render(node, var, val)
        for child in model.get_children():
            self.render(child, node)

        return node


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
        tree.write(filename)
