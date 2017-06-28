

class WritePv(object):
    """Action to write a value to a PV."""

    def __init__(self, pv, value, description=''):
        self.pv_name = pv
        self.description = description
        self.value = value
        self.timeout = 10


class ExecuteCommand(object):
    """Action to execute a shell command."""

    def __init__(self, command, description, directory="$(opi.dir)"):
        self.command = command
        self.description = description
        self.command_directory = directory
        self.wait_time = 10


class OpenOpi(object):
    """Action that opens another opi file."""

    REPLACE_CURRENT = 0
    WORKBENCH_TAB = 1
    WORKBENCH_TAB_LEFT = 2
    WORKBENCH_TAB_RIGHT = 3
    WORKBENCH_TAB_TOP = 4
    WORKBENCH_TAB_BOTTOM = 5
    DETACHED_TAB = 6
    NEW_WORKBENCH = 7
    STANDALONE = 8

    def __init__(self, path, mode=STANDALONE):
        """
        Construct OpenOpi action.

        Args:
            path of opi to open
            mode determining how the opi opens
        """
        self.path = path
        self.mode = mode


class Exit(object):
    """Action that closes the current opi."""
