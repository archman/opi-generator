import xml.etree.ElementTree as et


class Widget(object):

    def __init__(self, id, x, y, width, height, parent=None, name='widget'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._parent = parent
        self._children = []
        if self._parent is None:
            self._node = et.Element(name)
        else:
            self._node = et.SubElement(parent.get_node(), name)
            parent.add_child(self)
        self._node.set('typeId', id)

    def assemble(self):
        for child in self._children:
            child.assemble()
        for var, val in sorted(vars(self).iteritems()):
            if not var.startswith('_'):
                node = et.SubElement(self._node, var)
                node.text = str(val)

    def get_node(self):
        return self._node

    def add_child(self, child):
        self._children.append(child)

    def __str__(self):
        self.assemble()
        return et.tostring(self._node)

    def write_to_file(self, filename):
        self.assemble()
        tree = et.ElementTree(self._node)
        tree.write(filename)


class Display(Widget):

    ID = 'org.csstudio.opibuilder.Display'

    def __init__(self, width, height):
        super(Display, self).__init__(Display.ID, 0, 0, width, height,
                                      parent=None, name='display')
        self.auto_zoom_to_fit_all = 'false'
        self.show_grid = 'true'


class Rectangle(Widget):

    ID = 'org.csstudio.opibuilder.widgets.Rectangle'

    def __init__(self, x, y, width, height, parent):
        super(Rectangle, self).__init__(Rectangle.ID, x, y, width, height, parent)


