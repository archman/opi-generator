"""Class that renders scripts for a widget in CS-Studio"""

from lxml import etree as et


class OpiScripts:
    """Class that renders scripts for a widget in CS-Studio"""

    def render(self, widget_node, tag_name, scripts_model):
        """Does actual rendering"""

        if len(scripts_model) != 0:
            scripts_node = et.SubElement(widget_node, "scripts")
            for script_path, pvs, embed in scripts_model:
                # Embedded Script
                if embed:
                    # Create a path_node with specific attributes
                    path_node = et.SubElement(scripts_node,
                                              "path",
                                              pathString="EmbeddedPy",
                                              checkConnect="true",
                                              sfe="false",
                                              seoe="false")

                    # Add the script name
                    et.SubElement(path_node, "scriptName").text = script_path

                    # Read the script file and embed it into the XML
                    with open(script_path, 'r', encoding="utf-8") as file:
                        script_text = file.read()

                    et.SubElement(path_node, "scriptText").text = et.CDATA(script_text)

                # Non-embedded script
                else:
                    path_node = et.SubElement(scripts_node, "path")
                    path_node.set("pathString", script_path)

                # Add the PVs
                for process_variable, trigger in pvs:
                    et.SubElement(path_node, "pv", trig=str(trigger)).text = str(process_variable)
