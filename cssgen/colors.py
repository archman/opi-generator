import xml.etree.ElementTree as et


class OpiColorRenderer(object):

    def render(self, color_node, color_model):
        color_node = et.SubElement(color_node, 'color')
        color_node.set('red', str(color_model.red))
        color_node.set('green', str(color_model.green))
        color_node.set('blue', str(color_model.blue))
        if color_model.name is not None:
            color_node.set('name', color_model.name)
