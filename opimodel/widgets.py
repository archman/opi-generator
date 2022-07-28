"""
Module containing widgets to describe opi files.  An opi has a root widget
of type Display.  To create the opi, add widgets as children of this widget.
"""
from opimodel import actions, scalings
from opimodel.colors import Color
from opimodel.colors import DEFAULT_DISPLAY_BG, DEFAULT_TEXTUPDATE_BG, DEFAULT_TEXTINPUT_BG


class ResizeBehaviour:
    # for LinkingContainer
    RESIZE_OPI_TO_FIT_CONTAINER = 0 # Size *.opi to fit the container
    RESIZE_CONTAINER_TO_FIT_OPI = 1 # Size the container to fit *.opi
    CROP = 2     # Don't resize anything, crop if *.opi too large
    SCROLL = 3   # Don't resize anything, add scrollbars if *.opi too large


class FormatType:
    DEFAULT = 0
    DECIMAL = 1
    EXPONENTIAL = 2
    HEX_32 = 3
    STRING = 4
    HEX_64 = 5
    COMPACT = 6
    ENGINEERING = 7
    SEXAGESIMAL = 8
    SEXAGESIMAL_HMS = 9
    SEXAGESIMAL_DMS = 10


class BasicStyle:
    # ActionButton, TextInput
    CLASSIC = 0
    NATIVE = 1


class HAlign:
    """Enum describing horizontal alignment

    This is typically used with the horizontal_alignment property.
    """
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class VAlign:
    """Enum describing vertical alignment

    This is typically used with the vertical_alignment property.
    """
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2

HA_RIGHT = HAlign.RIGHT
HA_CENTER = HAlign.CENTER
HA_LEFT = HAlign.LEFT
VA_TOP = VAlign.TOP
VA_MIDDLE = VAlign.MIDDLE
VA_BOTTOM = VAlign.BOTTOM


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
        self._type_id = type_id
        self.rules = []

    def get_name(self):
        return self._name

    def get_type_id(self):
        return self._type_id

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

    def add_rule(self, rule):
        """Add a rule to the widget.

        Args:
            Rule object
        """
        self.rules.append(rule)

    def add_scale_options(self, width=True, height=True, keep_wh_ratio=False):
        """Add scale options to the widget.

        Args:
            width (bool): True if widget width is scalable
            height (bool): True if widget height is scalable
            keep_wh_ratio (bool):
        """
        self.scale_options = scalings.ScaleOptions(width, height, keep_wh_ratio)


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

    def add_open_opi(self, path, mode=actions.OpenOpi.STANDALONE, description=None, macros=None, parent_macros=True):
        self.actions.add_action(actions.OpenOpi(path, mode, description, macros, parent_macros))

    def add_exit(self):
        self.actions.add_action(actions.Exit())

    def set_basic_style(self, style):
        # does not work well
        if style == BasicStyle.CLASSIC:
            self.alarm_pulsing = False
            self.backcolor_alarm_sensitive = False
            self.set_bg_color(Color((218, 218, 218), 'ControlAndButtons Background'))
            self.style = style
        else: # NATIVE
            self.style = style


class Display(Widget):
    """
    Display widget.  This is the root widget for any opi.
    """

    TYPE_ID = 'org.csstudio.opibuilder.Display'

    def __init__(self, width=800, height=600):
        super(Display, self).__init__(Display.TYPE_ID, 0, 0, width, height,
                                      name='display')
        self.auto_zoom_to_fit_all = False
        self.show_grid = True
        self.set_bg_color(DEFAULT_DISPLAY_BG)

    def add_scale_options(self, min_width=-1, min_height=-1, autoscale=False):
        """Add scale options to the display.

        Args:
            min_width (int): Display min width, -1 for no scaling
            min_height (int): Display min height, -1 for no scaling
            autoscale (bool): Autoscale child widgets
        """
        self.auto_scale_widgets = scalings.DisplayScaleOptions(min_width, min_height, autoscale)


class Rectangle(ActionWidget):

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
        self.set_bg_color(DEFAULT_TEXTUPDATE_BG)

TextUpdate = TextMonitor


class TextInput(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.TextInput'

    def __init__(self, x, y, width, height, pv, style=None):
        super(TextInput, self).__init__(
            TextInput.TYPE_ID, x, y, width, height)

        self.pv_name = pv
        self.horizontal_alignment = HAlign.CENTER
        self.set_bg_color(DEFAULT_TEXTINPUT_BG)
        if style is not None:
            self.set_basic_style(style)

TextEntry = TextInput


class GroupingContainer(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.groupingContainer'

    def __init__(self, x, y, width, height):
        super(GroupingContainer, self).__init__(
            GroupingContainer.TYPE_ID, x, y, width, height)
        self.lock_children = True
        self.transparent = True
        self.set_bg_color(DEFAULT_DISPLAY_BG)


class TabbedContainer(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.tab'

    def __init__(self, x, y, width, height):
        super(TabbedContainer, self).__init__(
            TabbedContainer.TYPE_ID, x, y, width, height)
        self.transparent = True
        self.tab_count = 0

    def add_tab(self, name, widget, dw=2, dh=33):
        """Add a new tab named as *name*, embbed with *widget*.

        _grp.width = self.width - dw
        _grp.height = self.height - dh
        """
        setattr(self, f"tab_{self.tab_count}_title", name)
        _grp = GroupingContainer(1, 1, self.width - dw, self.height - dh)
        _grp.name = name
        _grp.add_child(widget)
        self.add_child(_grp)
        self.tab_count += 1

    def set_font(self, font):
        """Set font for each tab. Call this method after added all tabs.
        """
        for i in range(self.tab_count):
            setattr(self, f"tab_{i}_font", font)


class LinkingContainer(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.linkingContainer'

    def __init__(self, x, y, width, height, opi_file):
        super(LinkingContainer, self).__init__(
            LinkingContainer.TYPE_ID, x, y, width, height)
        self.opi_file = opi_file
        self.resize_behaviour = ResizeBehaviour.CROP
        self.set_bg_color(DEFAULT_DISPLAY_BG)


class ActionButton(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.ActionButton'

    def __init__(self, x, y, width, height, text, style=None, hook_first=True, hook_all=False):
        super(ActionButton, self).__init__(
            ActionButton.TYPE_ID, x, y, width, height, hook_first, hook_all)

        self.text = text
        if style is not None:
            self.set_basic_style(style)


class MenuButton(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.MenuButton'

    def __init__(self, x, y, width, height, text):
        super(MenuButton, self).__init__(
            MenuButton.TYPE_ID, x, y, width, height)

        self.label = text


class CheckBox(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.checkbox'

    def __init__(self, x, y, width, height, text, pv_name):
        super(CheckBox, self).__init__(
            CheckBox.TYPE_ID, x, y, width, height)

        self.label = text
        self.pv_name = pv_name


class ToggleButton(ActionWidget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.BoolButton'

    def __init__(self, x, y, width, height, on_text, off_text, pv_name=None):
        super(ToggleButton, self).__init__(
            ToggleButton.TYPE_ID, x, y, width, height)

        if pv_name is not None:
            self.pv_name = pv_name

        self.on_label = on_text
        self.off_label = off_text
        self.toggle_button = True
        self.effect_3d = True
        self.square_button = True
        self.show_boolean_label = True
        self.show_led = False
        self.push_action_index = 0
        self.released_action_index = 1

    def add_push_action(self, action):
        self.actions.add_action(action)
        self.push_action_index = len(self.actions) - 1

    def add_release_action(self, action):
        self.actions.add_action(action)
        self.released_action_index = len(self.actions) - 1


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


class Symbol(ActionWidget):
    TYPE_ID = 'org.csstudio.opibuilder.widgets.edm.symbolwidget'

    def __init__(self, x, y, width, height, pv, image_file, image_width, image_index=0):
        super(Symbol, self).__init__(Symbol.TYPE_ID, x, y, width, height)
        self.pv_name = pv
        self.image_file = image_file
        self.image_index = image_index
        self.sub_image_width = image_width


# Tank
class Tank(Widget):

    TYPE_ID = 'org.csstudio.opibuilder.widgets.tank'

    def __init__(self, x, y, width, height, pv):
        super(Tank, self).__init__(Tank.TYPE_ID, x, y, width, height)
        self.pv_name = pv
        self.effect_3d = False


class DataBrowser(Widget):

    TYPE_ID = 'org.csstudio.trends.databrowser.opiwidget'

    def __init__(self, x, y, width, height, filename):
        super(DataBrowser, self).__init__(DataBrowser.TYPE_ID, x, y, width, height)
        self.filename = filename
