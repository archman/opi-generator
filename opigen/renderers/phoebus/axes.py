"""Class that renders the axes of graphs in Phoebus"""

from lxml import etree as et


class OpiAxis:
    """Class that renders the axes of graphs in Phoebus"""

    def _render_axis(self, parent_node, axis_name, axis_values):
        """Helper function to render individual axis"""
        axis_node = et.SubElement(parent_node, axis_name)
        for key, value in zip(['title', 'autoscale', 'minimum', 'maximum'], axis_values):
            et.SubElement(axis_node, key).text = str(value)

    def render(self, widget_node, tag_name, axes_model):
        """Does actual rendering"""
        # Render X-axis
        self._render_axis(widget_node, "x_axis", axes_model[0])

        # Create root node for y-axes
        y_axes_root_node = et.SubElement(widget_node, "y_axes")

        # Render y-axes
        for axis_values in axes_model[1:]:
            self._render_axis(y_axes_root_node, "y_axis", axis_values)
