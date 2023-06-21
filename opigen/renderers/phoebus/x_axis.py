"""Class that renders the X-Axis of graphs in Phoebus"""

from lxml import etree as et


class OpiXAxis(object):
    """Class that renders the X-Axis of graphs in Phoebus"""

    def render(self, widget_node, tag_name, x_axis_model):
        """Does actual rendering"""
        x_axis_node = et.SubElement(widget_node, "x_axis")
        axis_title, minimum, maximum, auto_scale = x_axis_model
        et.SubElement(x_axis_node, 'title').text = str(axis_title)
        et.SubElement(x_axis_node, 'autoscale').text = str(auto_scale)
        et.SubElement(x_axis_node, 'minimum').text = str(minimum)
        et.SubElement(x_axis_node, 'maximum').text = str(maximum)
