import lxml.etree as et


class OpiActionRenderer(object):

    def render(self, widget_node, tag_name, action_list):
        actions_node = et.SubElement(widget_node, tag_name)
        for action_model in action_list:
            self.render_one(actions_node, action_model)

    def render_one(self, actions_node, action_model):
            action_node = et.SubElement(actions_node, 'action')
            action_node.set('type', action_model._action_type)
            for key, value in vars(action_model).items():
                if not key.startswith('_'):
                    n = et.SubElement(action_node, key)
                    n.text = str(value)
