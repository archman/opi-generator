from model import actions


class WidgetModel(object):

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

    def get_children(self):
        return self._children


class DisplayModel(WidgetModel):

    ID = 'org.csstudio.opibuilder.Display'

    def __init__(self, width, height):
        super(DisplayModel, self).__init__(DisplayModel.ID, 0, 0, width, height,
                                           name='display')
        self.auto_zoom_to_fit_all = False
        self.show_grid = True


class RectangleModel(WidgetModel):

    ID = 'org.csstudio.opibuilder.widgets.Rectangle'

    def __init__(self, x, y, width, height):
        super(RectangleModel, self).__init__(RectangleModel.ID, x, y,
                                             width, height)


class GroupingContainerModel(WidgetModel):

    ID = 'org.csstudio.opibuilder.widgets.groupingContainer'

    def __init__(self, x, y, width, height):
        super(GroupingContainerModel, self).__init__(GroupingContainerModel.ID,
                                                     x, y, width, height)


class ActionButtonModel(WidgetModel):

    ID = 'org.csstudio.opibuilder.widgets.ActionButton'

    def __init__(self, x, y, width, height, text):
        super(ActionButtonModel, self).__init__(ActionButtonModel.ID, x, y,
                                                width, height)
        self.text = text
        self.actions = []

    def add_write_pv(self, pv, value):
        self.actions.append(actions.WritePvAction(pv, value))

    def add_shell_command(self, command, directory="$(opi.dir)"):
        self.actions.append(actions.ExecuteCommandAction(command, directory))
