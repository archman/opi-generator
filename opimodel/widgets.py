from opimodel import actions


class HAlign(object):  # pragma pylint: disable=too-few-public-methods
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class Widget(object):

    def __init__(self, type_id, x, y, width, height, name='widget'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._name = name
        self._children = []
        self._parent = None
        self._typeId = type_id

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def add_child(self, child):
        self._children.append(child)
        child.set_parent(self)

    def add_children(self, children):
        for child in children:
            self.add_child(child)

    def get_children(self):
        return self._children

    def set_bg_color(self, color):
        self.background_color = color

    def set_fg_color(self, color):
        self.foreground_color = color

    def set_border(self, border):
        self.border = border

    def set_font(self, font):
        self.font = font


class ActionWidget(Widget):

    # No ID, designed to be subclassed only
    def __init__(self, type_id, x, y, width, height):
        super(ActionWidget, self).__init__(type_id, x, y, width, height)
        self.actions = []

    def add_action(self, action):
        """
        Add any action to the list of actions.

        Args:
            action to add
        """
        self.actions.append(action)

    def add_write_pv(self, pv, value, description=""):
        self.actions.append(actions.WritePv(pv, value, description))

    def add_shell_command(
            self, command, description="", directory="$(opi.dir)"):
        self.actions.append(actions.ExecuteCommand(
                command, description, directory))

    def add_open_opi(self, path, mode=actions.OpenOpi.STANDALONE):
        self.actions.append(actions.OpenOpi(path, mode))


class Display(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.Display'

    def __init__(self, width, height):
        super(Display, self).__init__(Display.TYPE_ID, 0, 0, width, height,
                                      name='display')
        self.auto_zoom_to_fit_all = False
        self.show_grid = True


class Rectangle(Widget):

    ID = 'org.csstudio.opibuilder.widgets.Rectangle'

    def __init__(self, x, y, width, height):
        super(Rectangle, self).__init__(Rectangle.ID, x, y, width, height)


class Label(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.Label'

    def __init__(self, x, y, width, height, text):
        super(Label, self).__init__(Label.TYPE_ID, x, y, width, height)
        self.text = text


class TextMonitor(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.TextUpdate'

    def __init__(self, x, y, width, height, pv):
        super(TextMonitor, self).__init__(TextMonitor.TYPE_ID, x, y, width, height)
        self.pv_name = pv
        self.horizontal_alignment = HAlign.CENTER


class TextInput(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.TextInput'

    def __init__(self, x, y, width, height, pv):
        super(TextInput, self).__init__(TextInput.TYPE_ID, x, y, width, height)
        self.pv_name = pv


class GroupingContainer(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.groupingContainer'

    def __init__(self, x, y, width, height):
        super(GroupingContainer, self).__init__(GroupingContainer.TYPE_ID,
                                                x, y, width, height)


class ActionButton(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.ActionButton'

    def __init__(self, x, y, width, height, text):
        super(ActionButton, self).__init__(ActionButton.TYPE_ID, x, y, width, height)
        self.text = text


class MenuButton(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.MenuButton'

    def __init__(self, x, y, width, height, text):
        super(MenuButton, self).__init__(MenuButton.TYPE_ID, x, y, width, height)
        self.label = text


class ToggleButton(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.BoolButton'

    def __init__(self, x, y, width, height, on_text, off_text):
        super(ToggleButton, self).__init__(ToggleButton.TYPE_ID, x, y, width, height)
        self.actions = []
        self.on_label = on_text
        self.off_label = off_text
        self.toggle_button = True
        self.effect_3d = True
        self.square_button = True
        self.show_boolean_label = True
        self.show_led = False

    def add_push_action(self, action):
        self.actions.append(action)
        self.push_action_index = len(self.actions) - 1

    def add_release_action(self, action):
        self.actions.append(action)
        self.release_action_index = len(self.actions) - 1


class Led(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.LED'

    def __init__(self, x, y, width, height, pv):
        super(Led, self).__init__(Led.TYPE_ID, x, y, width, height)
        self.pv_name = pv
