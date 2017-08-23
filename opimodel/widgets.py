"""
Module containing widgets to describe opi files.  An opi has a root widget
of type Display.  To create the opi, add widgets as children of this widget.
"""
from opimodel import actions


class HAlign(object):
    """Enum describing horizontal alignment, typically used with the
       horizontal_alignment property.
    """
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class Widget(object):
    """Base class for any widget to extend.

    Args:
        id - the CSS id for the widget.
        x - the x position of the widget in pixels
        y - the y position of the widget in pixels
        widget - the width of the widget in pixels
        height - the height of the widget in pixels
        name - a name for the widget within the display
    """

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
        """Get the parent widget of this widget.
        """
        return self._parent

    def set_parent(self, parent):
        """Set the parent widget of this widget.

        Args:
            widget to be this widget's parent
        """
        self._parent = parent

    def add_child(self, child):
        """Add a widget as a child of this widget.

        Args:
            child widget
        """
        self._children.append(child)
        child.set_parent(self)

    def add_children(self, children):
        """Add multiple widgets as children of this widget.

        Args:
            sequence of child widgets
        """
        for child in children:
            self.add_child(child)

    def get_children(self):
        """Get all child widgets.
        """
        return self._children

    def set_bg_color(self, color):
        """Set background color for the widget.

        Args:
            Color object
        """
        self.background_color = color

    def set_fg_color(self, color):
        """Set background color for the widget.

        Args:
            Color object
        """
        self.foreground_color = color

    def set_border(self, border):
        """Set border for the widget.

        Args:
            Border object
        """
        self.border = border

    def set_font(self, font):
        """Set font for the widget.

        Args:
            Font object
        """
        self.font = font


class ActionWidget(Widget):
    """
    Base class for any widget that can have a list of actions.
    """

    # No ID, designed to be subclassed only
    def __init__(self, type_id, x, y, width, height, hook_first=True, hook_all=False):
        super(ActionWidget, self).__init__(type_id, x, y, width, height)
        self.actions = actions.ActionsModel(hook_first, hook_all)

    def add_action(self, action):
        """
        Add any action to the list of actions.

        Args:
            action to add
        """
        self.actions.add_action(action)

    def add_write_pv(self, pv, value, description=""):
        self.actions.add_action(actions.WritePv(pv, value, description))

    def add_shell_command(
            self, command, description="", directory="$(opi.dir)"):
        self.actions.add_action(actions.ExecuteCommand(
                command, description, directory))

    def add_open_opi(self, path, mode=actions.OpenOpi.STANDALONE, macros=None, parent_macros=True):
        self.actions.add_action(actions.OpenOpi(path, mode, macros, parent_macros))

    def add_exit(self):
        self.actions.add_action(actions.Exit())


class Display(Widget):
    """
    Display widget.  This is the root widget for any opi.
    """

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


class Line(Widget):

    ID = 'org.csstudio.opibuilder.widgets.polyline'

    def __init__(self, x0, y0, x1, y1):
        """ Widget x,y location is calculated to be the top-left corner of
            rectangle defined by the diagonal from (x0, y0) to (x1, y1).
            The width and height are the lengths of the sides.
        """
        super(Line, self).__init__(
            Line.ID, x=min(x0, x1), y=min(y0, y1),
            width=abs(x0 - x1) + 1, height=abs(y0 - y1) + 1)
        self.points = [(x0, y0), (x1, y1)]


class Label(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.Label'

    def __init__(self, x, y, width, height, text):
        super(Label, self).__init__(Label.TYPE_ID, x, y, width, height)
        self.text = text


class TextMonitor(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.TextUpdate'

    def __init__(self, x, y, width, height, pv):
        super(TextMonitor, self).__init__(
            TextMonitor.TYPE_ID, x, y, width, height)

        self.pv_name = pv
        self.horizontal_alignment = HAlign.CENTER


class TextInput(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.TextInput'

    def __init__(self, x, y, width, height, pv):
        super(TextInput, self).__init__(
            TextInput.TYPE_ID, x, y, width, height)

        self.pv_name = pv


class GroupingContainer(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.groupingContainer'

    def __init__(self, x, y, width, height):
        super(GroupingContainer, self).__init__(
            GroupingContainer.TYPE_ID, x, y, width, height)


class ActionButton(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.ActionButton'

    def __init__(self, x, y, width, height, text, hook_first=True, hook_all=False):
        super(ActionButton, self).__init__(
            ActionButton.TYPE_ID, x, y, width, height, hook_first, hook_all)

        self.text = text


class MenuButton(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.MenuButton'

    def __init__(self, x, y, width, height, text):
        super(MenuButton, self).__init__(
            MenuButton.TYPE_ID, x, y, width, height)

        self.label = text


class ToggleButton(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.BoolButton'

    def __init__(self, x, y, width, height, on_text, off_text):
        super(ToggleButton, self).__init__(
            ToggleButton.TYPE_ID, x, y, width, height)

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


class Byte(Widget):
    TYPE_ID = 'org.csstudio.opibuilder.widgets.bytemonitor'

    def __init__(self, x, y, width, height, pv, bits, start_bit=None):
        super(Byte, self).__init__(Byte.TYPE_ID, x, y, width, height)
        self.pv_name = pv
        self.effect_3d = False
        self.square_led = True
        self.numBits = bits
        self.led_border = 1
        self.border_alarm_sensitive = False
        self.led_packed = True
        if start_bit is not None:
            self.startBit = start_bit
