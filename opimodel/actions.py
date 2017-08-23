
class ActionsModel(object):
    """
    Represents all actions attached to a widget.
    """

    def __init__(self, hook_first=True, hook_all=False):
        """
        Args:
            hook_first: whether first action is executed on mouse click
            hook_all: whether all actions are executed on mouse click
        """
        self._actions = []
        self._hook_first = hook_first
        self._hook_all = hook_all

    def add_action(self, action):
        self._actions.append(action)

    def set_hook_first(self, hook_first):
        self._hook_first = hook_first

    def get_hook_first(self):
        return self._hook_first

    def set_hook_all(self, hook_all):
        self._hook_all = hook_all

    def get_hook_all(self):
        return self._hook_all

    def __getitem__(self, index):
        return self._actions[index]

    def __len__(self):
        return len(self._actions)


class WritePv(object):
    """
    Action that writes the specified value to a named PV.
    """

    def __init__(self, pv, value, description=''):
        """
        Construct WritePv action.

        Args:
            pv name of PV to write, this can include macros
            value to write
            description to display
        """
        self.pv_name = pv
        self.description = description
        self.value = value
        self.timeout = 10


class ExecuteCommand(object):
    """
    Action that executes a script command in the specified directory.
    """

    OPI_DIR = '$(opi.dir)'
    HOME_DIR = '$(user.home)'

    def __init__(self, command, description, directory=OPI_DIR):
        """
        Construct ExecuteCommand action.

        The directory can be a real path or one of the predefined helper macros:
            OPI_DIR: the directory containing the OPI file
            HOME_DIR: users home directory

        Args:
            command to execute
            description to display
            directory to execute the script
        """
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

    def __init__(self, path, mode=STANDALONE, macros=None, parent_macros=True):
        """
        Construct OpenOpi action.

        Args:
            path of opi to open
            mode determining how the opi opens
            macros: dict of macros with which to open the opi
            parent_macros: whether to inherit parent macros
        """
        self.path = path
        self.mode = mode
        self._macros = {} if macros is None else macros
        self._parent_macros = parent_macros

    def get_macros(self):
        return self._macros

    def get_parent_macros(self):
        return self._parent_macros


class Exit(object):
    """Action that closes the current opi."""
