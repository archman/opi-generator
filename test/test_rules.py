from utils import widget
from cssgen import nodes
from cssgen import rules


def test_empty_RulesNode(widget):
    widget.rules = nodes.ListNode()
    output = str(widget)
    assert '<rules />' in output


def test_greater_than_rule(widget):
    widget.rules = nodes.ListNode()
    widget.rules.add_child(rules.GreaterThanRuleNode('vis', 'dummy_pv', '0'))
    widget.assemble()
    rule_element = widget.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 > 0'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'true'
    assert exp_elements[1].attrib['bool_exp'] == 'true'


def test_between_rule(widget):
    widget.rules = nodes.ListNode()
    widget.rules.add_child(rules.BetweenRuleNode('vis', 'dummy_pv', '0', '5'))
    widget.assemble()
    rule_element = widget.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 3
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 < 0'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'false'
    assert exp_elements[1].attrib['bool_exp'] == 'pv0 > 5'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'
    assert exp_elements[2].attrib['bool_exp'] == 'true'
