import xml.etree.ElementTree as et
from cssgen import nodes, actions, rules


class OPIRenderer(object):

    def __init__(self, model):
        self._model = model
        self._node = None

    def assemble(self, model=None, parent=None):
        if model is None:
            model = self._model
        if parent is None:
            node = et.Element(model._name)
        else:
            node = et.SubElement(parent, model._name)
        for var, val in sorted(vars(model).items()):
            if not var.startswith('_'):
                if var == 'actions':
                    child_node = et.SubElement(node, var)
                    action_renderer = actions.OpiActionRenderer()
                    for action in val:
                        action_renderer.render(child_node, action)
                elif var == 'rules':
                    child_node = et.SubElement(node, var)
                    rules_renderer = rules.OpiRuleRenderer()
                    for rule in val:
                        rules_renderer.render(child_node, rule)
                    pass
                else:
                    child_node = et.SubElement(node, var)
                    nodes.TextNode(val).render(child_node)
        node.set('typeId', model._typeId)
        for child in model.get_children():
            self.assemble(child, node)

        if parent is None:
            self._node = node

    def get_node(self):
        return self._node

    def __str__(self):
        self.assemble()
        return str(et.tostring(self._node))

    def write_to_file(self, filename):
        self.assemble()
        tree = et.ElementTree(self._node)
        tree.write(filename)
