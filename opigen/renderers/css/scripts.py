"""Class that renders scripts for a widget in CS-Studio"""

from lxml import etree as et


class OpiScripts:
    """Class that renders scripts for a widget in CS-Studio"""

    def render(self, widget_node, tag_name, scripts_model):
        """Does actual rendering"""

        if len(scripts_model) != 0:
            scripts_node = et.SubElement(widget_node, "scripts")
            for script_path, pvs in scripts_model:
                path_node = et.SubElement(scripts_node, "path")
                path_node.set("pathString", script_path)

                for pv in pvs:
                    et.SubElement(path_node, "pv").text = str(pv)
