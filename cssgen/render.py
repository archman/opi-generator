import xml.etree.ElementTree as et
from cssgen import actions, rules, colors
import collections


def get_opi_renderer(widget):
    ar = actions.OpiActionRenderer()
    rr = rules.OpiRuleRenderer()
    tr = OpiTextRenderer()
    cr = colors.OpiColorRenderer()
    wr = OpiWidgetRenderer(ar, rr, tr, cr)
    return OpiRenderer(widget, wr)


class OpiTextRenderer(object):

    def render(self, text_node, model):
        if model is True:
            text_node.text = 'true'
        elif model is False:
            text_node.text = 'false'
        else:
            text_node.text = str(model)


class OpiWidgetRenderer(object):

    def __init__(self, action_renderer, rule_renderer, text_renderer, color_renderer):
        self._action_renderer = action_renderer
        self._rule_renderer = rule_renderer
        self._text_renderer = text_renderer
        self._color_renderer = color_renderer
        self._renderers = collections.defaultdict(lambda: self._text_renderer)
        self._renderers['actions'] = self._action_renderer
        self._renderers['rules'] = self._rule_renderer
        self._renderers['background_color'] = self._color_renderer
        self._renderers['foreground_color'] = self._color_renderer

    def render(self, model, parent):
        if parent is None:
            node = et.Element(model._name)
        else:
            node = et.SubElement(parent, model._name)
        node.set('typeId', model._typeId)
        for var, val in sorted(vars(model).items()):
            if not var.startswith('_'):
                child_node = et.SubElement(node, var)
                self._renderers[var].render(child_node, val)
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
