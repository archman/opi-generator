"""Classes for creating scripts to pass to widgets."""


class Script:
    """Represents a script to be added to a widget.

    Attributes:
        script_path (str): The file path to the location of the script.
        embed (bool): Indicates whether the script should be embedded into XML.
        name (str): Name of the script. Defaults to the script filename.
        pvs (List[Tuple[str, bool]]): A list of process variables (PVs) associated with the script. 
            Each PV is represented as a tuple, where the first element is the PV name and the second 
            element is a boolean indicating whether this PV should trigger the script.
    """

    def __init__(self, script_path, embed=True, name=None):
        """Initializes the Script object.

        Args:
            script_path (str): The file path to the location of the script.
            embed (bool, optional): Indicates whether the script should be embedded into XML. 
                Defaults to True.
            name (str, optional): Name of the script. Defaults to the script's filename.
        """
        self.script_path = script_path
        self.embed = embed

        if name is not None:
            self.name = name
        elif name is None:
            # Formats the script path such that the name is only the file name without its file
            # extension.
            self.name = self.script_path.rsplit('/', 1)[-1].rsplit('.', 1)[0]

        self.pvs = []

    def add_pv(self, process_variable, trigger=True):
        """Adds a PV to the script's PV list.

        Args:
            process_variable (str): The PV to add.
            trigger (bool, optional): Indicates whether this PV should trigger the script. Defaults
                to True.
        """
        self.pvs.append((process_variable, trigger))
