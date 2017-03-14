from utils import widget
from cssgen import nodes
from cssgen import rules


def test_empty_RulesNode(widget):
    widget.rules = nodes.ListNode()
    output = str(widget)
    assert '<rules />' in output


def test_simple_rule(widget):
    widget.rules = nodes.ListNode()
    widget.rules.add_child(rules.RuleNode('vis', 'dummy_pv', 'pv0 > 0'))
    widget.assemble()
    rule_element = widget.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_element = rule_element.find('./exp')
    assert exp_element.attrib['bool_exp'] == 'pv0 > 0'
    value_element = exp_element.find('./value')
    assert value_element.text == 'true'
