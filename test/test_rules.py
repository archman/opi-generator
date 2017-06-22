from opimodel import rules
from renderers import render


def test_empty_RulesNode(widget, get_renderer):
    widget.rules = []
    renderer = get_renderer(widget)
    output = str(renderer)
    assert '<rules/>' in output


def test_greater_than_rule(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.GreaterThanRule('vis', 'dummy_pv', '0'))
    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 > 0'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'true'
    assert exp_elements[1].attrib['bool_exp'] == 'true'


def test_between_rule(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.BetweenRule('vis', 'dummy_pv', '0', '5'))
    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
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
