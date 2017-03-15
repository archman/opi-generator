

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
