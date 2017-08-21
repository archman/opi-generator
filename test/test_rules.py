from opimodel import rules, colors


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

def test_between_rule_gt_equals(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.BetweenRule(
        'vis', 'dummy_pv', '0', '5', gt_equals=True))
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
    assert exp_elements[1].attrib['bool_exp'] == 'pv0 >= 5'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'
    assert exp_elements[2].attrib['bool_exp'] == 'true'


def test_between_rule_lt_equals(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.BetweenRule(
        'vis', 'dummy_pv', '0', '5', lt_equals=True))
    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 3
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 <= 0'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'false'
    assert exp_elements[1].attrib['bool_exp'] == 'pv0 > 5'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'
    assert exp_elements[2].attrib['bool_exp'] == 'true'


def test_between_rule_gt_equals_and_lt_equals(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.BetweenRule(
        'vis', 'dummy_pv', '0', '5', gt_equals=True, lt_equals=True))
    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 3
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 <= 0'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'false'
    assert exp_elements[1].attrib['bool_exp'] == 'pv0 >= 5'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'
    assert exp_elements[2].attrib['bool_exp'] == 'true'


def test_selection_rule_one_string_value(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.SelectionRule(
        'test_property', 'dummy_pv', [('1', 'strval')]))

    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'strval'


def test_selection_rule_one_string_value_using_severity(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.SelectionRule(
        'test_property', 'dummy_pv', [('1', 'strval')], var=rules.PV_SEVR))

    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pvSev0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'strval'


def test_selection_rule_two_string_value(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.SelectionRule(
        'test_property', 'dummy_pv', [('1', 'val_one'), ('2', 'val_two')]))

    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pv0 == 2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_one_string_value_numeric_test(widget, get_renderer):
    widget.rules = []
    widget.rules.append(rules.SelectionRule(
        'test_property', 'dummy_pv', [(1, 'val_one')]))

    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'


def test_selection_rule_one_color_value(widget, get_renderer):

    col = colors.Color(rgb=(64, 128, 32), name="murky green")
    widget.rules = []
    widget.rules.append(rules.SelectionRule(
        'test_property', 'dummy_pv', [(1, col)]))

    renderer = get_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'

    color_element = exp_elements[0].find('./value/color')
    assert color_element.attrib['red'] == '64'
    assert color_element.attrib['green'] == '128'
    assert color_element.attrib['blue'] == '32'
    assert color_element.attrib['name'] == 'murky green'
