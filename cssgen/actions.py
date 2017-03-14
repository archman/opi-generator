from cssgen import widgets
from cssgen import nodes


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

    def __init__(self, x, y, width, height, text):
        super(ActionButton, self).__init__(ActionButton.ID, x, y,
                                           width, height)
        self.text = nodes.TextNode(text)
        self.actions = nodes.ActionsNode()

    def add_write_pv(self, pv, value):
        self.actions.add(WritePvAction(pv, value))

    def add_shell_command(self, command, directory="$(opi.dir)"):
        self.actions.add(ExecuteCommandAction(command, directory))
