class OpiBorderRenderer(object):

    def __init__(self, text_renderer, color_renderer):
        self._text_renderer = text_renderer
        self._color_renderer = color_renderer

    def render(self, widget_node, tag_name, border_model):
        self._text_renderer.render(widget_node, 'border_alarm_sensitive', border_model.alarm)
        self._text_renderer.render(widget_node, 'border_width', border_model.width)
        self._text_renderer.render(widget_node, 'border_style', border_model.style)
        self._color_renderer.render(widget_node, 'border_color', border_model.color)
