import xml.etree.ElementTree as et


class Node(object):

    def render(self, node):
        raise NotImplementedError('render() should be implemented')


class TextNode(Node):

    def __init__(self, value):
        self.value = value

    def render(self, parent_node):
        parent_node.text = str(self.value)


class ActionsNode(object):

    def __init__(self, parent):
        self._actions = []
        self._parent = parent

    def add(self, action):
        self._actions.append(action)

    def render(self, actions_node):
        for action in self._actions:
            action_node = et.SubElement(actions_node, 'action')
            action_node.set('type', action._action_type)
            print('adding action {}'.format(action))
            for key, value in vars(action).items():
                if not key.startswith('_'):
                    n = et.SubElement(action_node, key)
                    n.text = str(value)
