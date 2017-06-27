

class WritePv(object):

    def __init__(self, pv, value, description):
        self._action_type = 'WRITE_PV'
        self.pv_name = pv
        self.description = description
        self.value = value
        self.timeout = 10


class ExecuteCommand(object):

    def __init__(self, command, description, directory="$(opi.dir)"):
        self._action_type = 'EXECUTE_CMD'
        self.command = command
        self.description = description
        self.command_directory = directory
        self.wait_time = 10


class OpenOpi(object):

    REPLACE_CURRENT = 0
    WORKBENCH_TAB = 1
    WORKBENCH_TAB_LEFT = 2
    WORKBENCH_TAB_RIGHT = 3
    WORKBENCH_TAB_TOP = 4
    WORKBENCH_TAB_BOTTOM = 5
    DETACHED_TAB = 6
    NEW_WORKBENCH = 7
    STANDALONE = 8

    def __init__(self, path, mode):
        self._action_type = 'OPEN_DISPLAY'
        self.path = path
        self.mode = mode
