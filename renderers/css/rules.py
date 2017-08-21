import lxml.etree as et

from opimodel import rules, colors


class OpiRule(object):

    def __init__(self, color_renderer):
        self._color = color_renderer

    def render(self, widget_node, tag_name, rule_list):
        rules_node = et.SubElement(widget_node, tag_name)
        for rule_model in rule_list:
            self._render_one(rules_node, rule_model)

    def _render_one(self, rules_node, rule_model):
        self.rule_node = et.SubElement(rules_node, 'rule')
        self.rule_node.set('prop_id', rule_model._prop_id)
        self.rule_node.set('name', rule_model._name)
        if isinstance(rule_model, rules.BetweenRule):
            self._render_between(rule_model)
        elif isinstance(rule_model, rules.GreaterThanRule):
            self._render_greater_than(rule_model)
        elif isinstance(rule_model, rules.SelectionRule):
            self._render_selection(rule_model)

    def _render_between(self, rule_model):
        """ Write the between rule:
                true iff a < p < b
            as
                false if p <= a
                false if p >= b
                true otherwise

            if lower rule is 'a <= p' modify to be
                false if p < a

            if upper rule is 'p <= b' modify to be
                false if p > b

        """
        max_rule = 'pv0 {} {}'.format(
            ">" if rule_model._max_equals else ">=",
            rule_model._max)
        min_rule = 'pv0 {} {}'.format(
            "<" if rule_model._min_equals else "<=",
            rule_model._min)

        pv_node = et.SubElement(self.rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = rule_model._pv
        exp_node1 = et.SubElement(self.rule_node, 'exp')
        exp_node1.set('bool_exp', min_rule)
        val_node1 = et.SubElement(exp_node1, 'value')
        val_node1.text = 'false'
        exp_node2 = et.SubElement(self.rule_node, 'exp')
        exp_node2.set('bool_exp', max_rule)
        val_node2 = et.SubElement(exp_node2, 'value')
        val_node2.text = 'false'
        exp_node3 = et.SubElement(self.rule_node, 'exp')
        exp_node3.set('bool_exp', 'true')
        val_node3 = et.SubElement(exp_node3, 'value')
        val_node3.text = 'true'

    def _render_greater_than(self, rule_model):
        pv_node = et.SubElement(self.rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = rule_model._pv
        exp_node1 = et.SubElement(self.rule_node, 'exp')
        exp_node1.set('bool_exp', 'pv0 > {}'.format(rule_model._threshold))
        val_node1 = et.SubElement(exp_node1, 'value')
        val_node1.text = 'true'
        exp_node2 = et.SubElement(self.rule_node, 'exp')
        exp_node2.set('bool_exp', 'true')
        val_node2 = et.SubElement(exp_node2, 'value')
        val_node2.text = 'false'

    def _render_selection(self, rule_model):

        pv_node = et.SubElement(self.rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = rule_model._pv

        for (pv_val, prop_val) in rule_model._options:
            exp_node = et.SubElement(self.rule_node, 'exp')
            exp_node.set('bool_exp', '{} == {}'.format(rule_model._var, pv_val))
            if isinstance(prop_val, colors.Color):
                self._color.render(exp_node, 'value', prop_val)
            else:
                val_node = et.SubElement(exp_node, 'value')
                val_node.text = str(prop_val)
