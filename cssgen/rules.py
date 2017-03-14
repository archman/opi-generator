import xml.etree.ElementTree as et
from cssgen import nodes


class RuleNode(nodes.Node):

    def __init__(self, prop_id, pv, expression):
        self._prop_id = prop_id
        self._pv = pv
        self._expression = expression

    @staticmethod
    def escape_exp(exp):
        exp = exp.replace('>', '&gt;')
        exp = exp.replace('<', '&lt;')
        return exp

    def render(self, rules_node):
        rule_node = et.SubElement(rules_node, 'rule')
        rule_node.set('prop_id', self._prop_id)
        rule_node.set('name', 'Rule')
        pv_node = et.SubElement(rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = self._pv
        exp_node = et.SubElement(rule_node, 'exp')
        exp_node.set('bool_exp', self._expression)
        val_node = et.SubElement(exp_node, 'value')
        val_node.text = 'true'
