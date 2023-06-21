"""Class that renders the X-Axis of graphs in Phoebus"""

from lxml import etree as et


class OpiYAxis(object):
    """Class that renders the X-Axis of graphs in Phoebus"""

    def render(self, widget_node, tag_name, y_axes_model):
        """Does actual rendering"""
        if len(y_axes_model) > 0:
            y_axes_root_node = et.SubElement(widget_node, "y_axes")
            for axis_title, minimum, maximum, auto_scale in y_axes_model:
                y_axis_node = et.SubElement(y_axes_root_node, "y_axis")
                et.SubElement(y_axis_node, 'title').text = str(axis_title)
                et.SubElement(y_axis_node, 'autoscale').text = str(auto_scale)
                et.SubElement(y_axis_node, 'minimum').text = str(minimum)
                et.SubElement(y_axis_node, 'maximum').text = str(maximum)
