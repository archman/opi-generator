

class WritePvAction(object):

    def __init__(self, pv, value, description):
        self._action_type = 'WRITE_PV'
        self.pv_name = pv
        self.description = description
        self.value = value
        self.timeout = 10


class ExecuteCommandAction(object):

    def __init__(self, command, description, directory="$(opi.dir)"):
        self._action_type = 'EXECUTE_CMD'
        self.command = command
        self.description = description
        self.command_directory = directory
        self.wait_time = 10
