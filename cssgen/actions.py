import xml.etree.ElementTree as et
from cssgen import widgets
from cssgen import nodes


class ActionNode(nodes.Node):

    def render(self, actions_node):
        action_node = et.SubElement(actions_node, 'action')
        action_node.set('type', self._action_type)
        for key, value in vars(self).items():
            if not key.startswith('_'):
                n = et.SubElement(action_node, key)
                n.text = str(value)


class WritePvAction(ActionNode):

    def __init__(self, pv, value):
        self._action_type = 'WRITE_PV'
        self.pv_name = pv
        self.value = value
        self.timeout = 10


class ExecuteCommandAction(ActionNode):

    def __init__(self, command, directory="$(opi.dir)"):
        self._action_type = 'EXECUTE_CMD'
        self.command = command
        self.command_directory = directory
        self.wait_time = 10


class ActionButton(widgets.Widget):

    ID = 'org.csstudio.opibuilder.widgets.ActionButton'

    def __init__(self, x, y, width, height, text):
        super(ActionButton, self).__init__(ActionButton.ID, x, y,
                                           width, height)
        self.text = nodes.TextNode(text)
        self.actions = nodes.ListNode()

    def add_write_pv(self, pv, value):
        self.actions.add_child(WritePvAction(pv, value))

    def add_shell_command(self, command, directory="$(opi.dir)"):
        self.actions.add_child(ExecuteCommandAction(command, directory))
