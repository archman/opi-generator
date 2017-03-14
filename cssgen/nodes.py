

class Node(object):

    def render(self, node):
        raise NotImplementedError('render() should be implemented')


class TextNode(Node):

    def __init__(self, value):
        self.value = value

    def render(self, parent_node):
        parent_node.text = str(self.value)


class ListNode(Node):

    def __init__(self):
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def render(self, parent_node):
        for child in self._children:
            child.render(parent_node)
