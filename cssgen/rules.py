import xml.etree.ElementTree as et
from cssgen import nodes


class RuleNode(nodes.Node):

    def __init__(self, prop_id):
        self._prop_id = prop_id

    def render(self, rules_node):
        self.rule_node = et.SubElement(rules_node, 'rule')
        self.rule_node.set('prop_id', self._prop_id)
        self.rule_node.set('name', 'Rule')


class BetweenRuleNode(RuleNode):

    def __init__(self, prop_id, pv, min, max):
        super(BetweenRuleNode, self).__init__(prop_id)
        self._pv = pv
        self._min = min
        self._max = max

    def render(self, rules_node):
        super(BetweenRuleNode, self).render(rules_node)
        pv_node = et.SubElement(self.rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = self._pv
        exp_node1 = et.SubElement(self.rule_node, 'exp')
        exp_node1.set('bool_exp', 'pv0 < {}'.format(self._min))
        val_node1 = et.SubElement(exp_node1, 'value')
        val_node1.text = 'false'
        exp_node2 = et.SubElement(self.rule_node, 'exp')
        exp_node2.set('bool_exp', 'pv0 > {}'.format(self._max))
        val_node2 = et.SubElement(exp_node2, 'value')
        val_node2.text = 'false'
        exp_node3 = et.SubElement(self.rule_node, 'exp')
        exp_node3.set('bool_exp', 'true')
        val_node3 = et.SubElement(exp_node3, 'value')
        val_node3.text = 'true'


class GreaterThanRuleNode(RuleNode):

    def __init__(self, prop_id, pv, threshold):
        super(GreaterThanRuleNode, self).__init__(prop_id)
        self._pv = pv
        self._threshold = threshold

    def render(self, rules_node):
        super(GreaterThanRuleNode, self).render(rules_node)
        pv_node = et.SubElement(self.rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = self._pv
        exp_node1 = et.SubElement(self.rule_node, 'exp')
        exp_node1.set('bool_exp', 'pv0 > {}'.format(self._threshold))
        val_node1 = et.SubElement(exp_node1, 'value')
        val_node1.text = 'true'
        exp_node2 = et.SubElement(self.rule_node, 'exp')
        exp_node2.set('bool_exp', 'true')
        val_node2 = et.SubElement(exp_node2, 'value')
        val_node2.text = 'false'
