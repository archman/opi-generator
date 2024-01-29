""" Class that handles rendering of Traces. """

from lxml import etree as et


class OpiTraces(object):
    """Class that handles rendering of Traces."""

    def __init__(self, color_renderer):
        self._color = color_renderer

    def render(self, widget_node, tag_name, traces_model):
        """Renders the actual traces"""
        if len(traces_model) == 0:
            return
        trace_root_node = et.SubElement(widget_node, "traces")
        for widget_type, legend, x_pv, y_pv, trace_type, line_width, \
            line_style, point_type, point_size, y_axis, trace_color in traces_model:
            trace_node = et.SubElement(trace_root_node, "trace")
            et.SubElement(trace_node, "name").text = str(legend)
            if widget_type == "xyplot" and x_pv is not None:
                et.SubElement(trace_node, "x_pv").text = str(x_pv)
            et.SubElement(trace_node, "y_pv").text = str(y_pv)
            et.SubElement(trace_node, "axis").text = str(y_axis)
            et.SubElement(trace_node, "line_width").text = str(line_width)
            et.SubElement(trace_node, "line_style").text = str(line_style)
            et.SubElement(trace_node, "point_type").text = str(point_type)
            et.SubElement(trace_node, "point_size").text = str(point_size)
            et.SubElement(trace_node, "trace_type").text = str(
                trace_type)  # 5: Bar graph for Phoebus

            # None is passed as color if defaults wish to be used
            if trace_color is not None:
                self._color.render(trace_node, 'color', trace_color)
