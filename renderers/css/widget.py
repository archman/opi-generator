import collections

import lxml.etree as et


class OpiWidget(object):

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