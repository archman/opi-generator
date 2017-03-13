from cssgen import widgets
import xml.etree.ElementTree as et


class Actions(object):

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


class WritePvAction(object):

    def __init__(self, pv, value):
        self._action_type = 'WRITE_PV'
        self.pv_name = pv
        self.value = value
        self.timeout = 10


class ExecuteCommandAction(object):

    def __init__(self, command, directory="$(opi.dir)"):
        self._action_type = 'EXECUTE_CMD'
        self.command = command
        self.command_directory = directory
        self.wait_time = 10


class ActionButton(widgets.Widget):

    ID = 'org.csstudio.opibuilder.widgets.ActionButton'

    def __init__(self, x, y, width, height, parent, text):
        super(ActionButton, self).__init__(ActionButton.ID, x, y,
                                           width, height, parent)
        self.text = widgets.TextNode(text)
        self.actions = Actions(self)

    def add_write_pv(self, pv, value):
        self.actions.add(WritePvAction(pv, value))

    def add_shell_command(self, command, directory="$(opi.dir)"):
        self.actions.add(ExecuteCommandAction(command, directory))
