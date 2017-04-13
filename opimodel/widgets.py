from opimodel import actions


class HAlign(object):
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class Widget(object):

    def __init__(self, id, x, y, width, height, name='widget'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._name = name
        self._children = []
        self._parent = None
        self._typeId = id

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


class Display(Widget):

    ID = 'org.csstudio.opibuilder.Display'

    def __init__(self, width, height):
        super(Display, self).__init__(Display.ID, 0, 0, width, height,
                                      name='display')
        self.auto_zoom_to_fit_all = False
        self.show_grid = True


class Rectangle(Widget):

    ID = 'org.csstudio.opibuilder.widgets.Rectangle'

    def __init__(self, x, y, width, height):
        super(Rectangle, self).__init__(Rectangle.ID, x, y,
                                        width, height)


class Label(Widget):

    ID = 'org.csstudio.opibuilder.widgets.Label'

    def __init__(self, x, y, width, height, text):
        super(Label, self).__init__(Label.ID, x, y, width, height)
        self.text = text


class TextMonitor(Widget):

    ID = 'org.csstudio.opibuilder.widgets.TextUpdate'

    def __init__(self, x, y, width, height, pv):
        super(TextMonitor, self).__init__(TextMonitor.ID, x, y, width, height)
        self.pv_name = pv
        self.horizontal_alignment = HAlign.CENTER


class TextInput(Widget):

    ID = 'org.csstudio.opibuilder.widgets.TextInput'

    def __init__(self, x, y, width, height, pv):
        super(TextInput, self).__init__(TextInput.ID, x, y, width, height)
        self.pv_name = pv


class GroupingContainer(Widget):

    ID = 'org.csstudio.opibuilder.widgets.groupingContainer'

    def __init__(self, x, y, width, height):
        super(GroupingContainer, self).__init__(GroupingContainer.ID,
                                                x, y, width, height)


class ActionButton(Widget):

    ID = 'org.csstudio.opibuilder.widgets.ActionButton'

    def __init__(self, x, y, width, height, text):
        super(ActionButton, self).__init__(ActionButton.ID, x, y, width, height)
        self.text = text
        self.actions = []

    def add_write_pv(self, pv, value):
        self.actions.append(actions.WritePvAction(pv, value))

    def add_shell_command(self, command, directory="$(opi.dir)"):
        self.actions.append(actions.ExecuteCommandAction(command, directory))


class ToggleButton(Widget):

    ID = 'org.csstudio.opibuilder.widgets.BoolButton'

    def __init__(self, x, y, width, height, on_text, off_text):
        super(ToggleButton, self).__init__(ToggleButton.ID, x, y, width, height)
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
