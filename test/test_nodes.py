import pytest
from cssgen import nodes
from cssgen import widgets
from cssgen import rules


@pytest.fixture
def widget():
    return widgets.Widget('dummyid', 0, 0, 10, 10)


def test_widget_render_contains_dynamically_added_values(widget):
    widget.test = nodes.TextNode('dummy')
    output = str(widget)
    assert '<test>dummy</test>' in output


def test_empty_RulesNode(widget):
    widget.rules = nodes.ParentNode()
    output = str(widget)
    assert '<rules />' in output


def test_simple_rule(widget):
    widget.rules = nodes.ParentNode()
    widget.rules.add_child(rules.RuleNode('vis', 'dummy_pv', 'pv0 > 0'))
    widget.assemble()
    rule_element = widget.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_element = rule_element.find('./exp')
    assert exp_element.attrib['bool_exp'] == 'pv0 > 0'
    value_element = exp_element.find('./value')
    assert value_element.text == 'true'
