from opigen import rules, colors


def test_empty_RulesNode_does_not_create_rules_tag(widget, get_opi_renderer):
    renderer = get_opi_renderer(widget)
    output = str(renderer)
    assert 'rules' not in output


def test_greater_than_rule(widget, get_opi_renderer):
    widget.add_rule(
        rules.GreaterThanRule('vis', 'dummy_pv', '0', name="positive_rule"))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.attrib['prop_id'] == 'vis'
    assert rule_element.attrib['name'] == 'positive_rule'
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'
    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 > 0'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'true'
    assert exp_elements[1].attrib['bool_exp'] == 'true'


def test_greater_than_rule_default_name(widget, get_opi_renderer):
    widget.add_rule(rules.GreaterThanRule('vis', 'dummy_pv', '0'))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.attrib['prop_id'] == 'vis'
    assert rule_element.attrib['name'] == 'GreaterThanRule'


def test_greater_than_rule_sets_val(widget, get_opi_renderer):
    widget.add_rule(
        rules.GreaterThanRule('image_index', 'dummy_pv', '1', val=99))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.attrib['prop_id'] == 'image_index'
    assert rule_element.attrib['name'] == 'GreaterThanRule'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 > 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == '99'


def test_greater_than_rule_sets_false_val(widget, get_opi_renderer):
    widget.add_rule(
        rules.GreaterThanRule('image_index',
                              'dummy_pv',
                              '1',
                              val=99,
                              false_val=33))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.attrib['prop_id'] == 'image_index'
    assert rule_element.attrib['name'] == 'GreaterThanRule'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[1].attrib['bool_exp'] == 'true'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == '33'


def test_between_rule_both_closed_0_lte_x_lte_5(widget, get_opi_renderer):
    widget.add_rule(
        rules.BetweenRule('vis',
                          'dummy_pv',
                          '0',
                          '5',
                          name="betweenRule",
                          min_equals=True,
                          max_equals=True))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['name'] == 'betweenRule'

    assert rule_element.find('./pv').attrib['trig'] == 'true'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2

    assert exp_elements[0].attrib['bool_exp'] == 'pv0 >= 0 && pv0 <= 5'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'true'

    assert exp_elements[1].attrib['bool_exp'] == 'true'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'


def test_between_rule_default_name(widget, get_opi_renderer):
    widget.add_rule(rules.BetweenRule('vis', 'dummy_pv', '0', '5'))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.attrib['name'] == 'BetweenRule'


def test_between_rule_lower_half_closed_0_lte_x_lt_5(widget, get_opi_renderer):
    widget.add_rule(
        rules.BetweenRule('vis', 'dummy_pv', '0', '5', max_equals=False))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2

    assert exp_elements[0].attrib['bool_exp'] == 'pv0 >= 0 && pv0 < 5'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'true'

    assert exp_elements[1].attrib['bool_exp'] == 'true'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'


def test_between_rule_upper_half_closed_0_lt_x_lte_5(widget, get_opi_renderer):
    widget.add_rule(
        rules.BetweenRule('vis', 'dummy_pv', '0', '5', min_equals=False))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2

    assert exp_elements[0].attrib['bool_exp'] == 'pv0 > 0 && pv0 <= 5'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'true'

    assert exp_elements[1].attrib['bool_exp'] == 'true'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'


def test_between_rule_both_open_0_lt_x_lt_5(widget, get_opi_renderer):
    widget.add_rule(
        rules.BetweenRule('vis',
                          'dummy_pv',
                          '0',
                          '5',
                          min_equals=False,
                          max_equals=False))
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.find('./pv').attrib['trig'] == 'true'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2

    assert exp_elements[0].attrib['bool_exp'] == 'pv0 > 0 && pv0 < 5'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'true'

    assert exp_elements[1].attrib['bool_exp'] == 'true'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'false'


def test_selection_rule_one_string_value(widget, get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'strval')],
                            name="stringSelection"))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['name'] == 'stringSelection'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'strval'


def test_selection_rule_one_string_value_phoebus(widget, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'strval')],
                            name="stringSelection"))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['name'] == 'stringSelection'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'strval'


def test_selection_rule_out_exp(widget, get_opi_renderer, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('true', 'pvStr0')],
                            name="outStr0",
                            out_exp="true",
                            auto_fill_val=False))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['name'] == 'outStr0'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'true'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'true'
    value_element = exp_elements[0].find('./expression')
    assert value_element.text == 'pvStr0'

    #
    renderer1 = get_opi_renderer(widget)
    renderer1.assemble()
    rule_element1 = renderer1.get_node().find('./rules/rule')
    assert rule_element1.find('./pv').text == 'dummy_pv'
    assert rule_element1.attrib['name'] == 'outStr0'
    assert rule_element1.attrib['prop_id'] == 'test_property'
    assert rule_element1.attrib['out_exp'] == 'true'

    exp_elements1 = rule_element1.findall('./exp')
    assert len(exp_elements1) == 1
    assert exp_elements1[0].attrib['bool_exp'] == 'true'
    value_element1 = exp_elements1[0].find('./value')
    assert value_element1.text == 'pvStr0'


def test_selection_rule_auto_fill(widget, get_opi_renderer, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('pv0==1', 'strval')],
                            name="stringSelection",
                            auto_fill_val=False))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['name'] == 'stringSelection'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0==1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'strval'

    #
    renderer1 = get_opi_renderer(widget)
    renderer1.assemble()
    rule_element1 = renderer1.get_node().find('./rules/rule')
    assert rule_element1.find('./pv').text == 'dummy_pv'
    assert rule_element1.attrib['name'] == 'stringSelection'
    assert rule_element1.attrib['prop_id'] == 'test_property'
    assert rule_element1.attrib['out_exp'] == 'false'

    exp_elements1 = rule_element1.findall('./exp')
    assert len(exp_elements1) == 1
    assert exp_elements1[0].attrib['bool_exp'] == 'pv0==1'
    value_element1 = exp_elements1[0].find('./value')
    assert value_element1.text == 'strval'


def test_selection_rule_default_name(widget, get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'strval')]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.attrib['name'] == 'SelectionRule'


def test_selection_rule_default_name_phoebus(widget, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'strval')]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.attrib['name'] == 'SelectionRule'


def test_selection_rule_one_string_value_using_severity(
        widget, get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            sevr_options=[('1', 'strval')]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pvSev0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'strval'


def test_selection_rule_one_string_value_using_severity_phoebus(
        widget, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            sevr_options=[('1', 'strval')]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pvSev0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'strval'


def test_selection_rule_two_string_value(widget, get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'val_one'), ('2', 'val_two')]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pv0 == 2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_two_string_value_phoebus(widget, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'val_one'), ('2', 'val_two')]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pv0 == 2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_one_string_value_numeric_test(widget,
                                                      get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[(1, 'val_one')]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'


def test_selection_rule_one_string_value_numeric_test_phoebus(
        widget, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[(1, 'val_one')]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'


def test_selection_rule_one_color_value(widget, get_opi_renderer):
    col = colors.Color(rgb=(64, 128, 32), name="murky green")
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[(1, col)]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'

    color_element = exp_elements[0].find('./value/color')
    assert color_element.attrib['red'] == '64'
    assert color_element.attrib['green'] == '128'
    assert color_element.attrib['blue'] == '32'
    assert color_element.attrib['name'] == 'murky green'


def test_selection_rule_one_color_value_phoebus(widget, get_bob_renderer):
    col = colors.Color(rgb=(64, 128, 32), name="murky green")
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[(1, col)]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 1
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'

    color_element = exp_elements[0].find('./value/color')
    assert color_element.attrib['red'] == '64'
    assert color_element.attrib['green'] == '128'
    assert color_element.attrib['blue'] == '32'
    assert color_element.attrib['name'] == 'murky green'


def test_selection_rule_sets_else_condition_when_specified(
        widget, get_opi_renderer):
    col = colors.Color(rgb=(64, 128, 32), name="murky green")
    red = colors.Color(rgb=(255, 0, 0), name="red")
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[(1, col)],
                            else_val=red))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    assert exp_elements[1].attrib['bool_exp'] == 'true'

    color_element = exp_elements[0].find('./value/color')
    assert color_element.attrib['red'] == '64'
    assert color_element.attrib['green'] == '128'
    assert color_element.attrib['blue'] == '32'
    assert color_element.attrib['name'] == 'murky green'

    color_element = exp_elements[1].find('./value/color')
    assert color_element.attrib['red'] == '255'
    assert color_element.attrib['green'] == '0'
    assert color_element.attrib['blue'] == '0'
    assert color_element.attrib['name'] == 'red'


def test_selection_rule_sets_else_condition_when_specified_phoebus(
        widget, get_bob_renderer):
    col = colors.Color(rgb=(64, 128, 32), name="murky green")
    red = colors.Color(rgb=(255, 0, 0), name="red")
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[(1, col)],
                            else_val=red))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    assert exp_elements[1].attrib['bool_exp'] == 'true'

    color_element = exp_elements[0].find('./value/color')
    assert color_element.attrib['red'] == '64'
    assert color_element.attrib['green'] == '128'
    assert color_element.attrib['blue'] == '32'
    assert color_element.attrib['name'] == 'murky green'

    color_element = exp_elements[1].find('./value/color')
    assert color_element.attrib['red'] == '255'
    assert color_element.attrib['green'] == '0'
    assert color_element.attrib['blue'] == '0'
    assert color_element.attrib['name'] == 'red'


def test_selection_rule_two_string_val_options(widget, get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'val_one'), ('2', 'val_two')]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pv0 == 2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_two_string_val_options_phoebus(widget,
                                                       get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'val_one'), ('2', 'val_two')]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pv0 == 2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_two_string_sevr_options(widget, get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            sevr_options=[('1', 'val_one'), ('2', 'val_two')]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pvSev0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pvSev0 == 2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_two_string_sevr_options_phoebus(
        widget, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            sevr_options=[('1', 'val_one'), ('2', 'val_two')]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 2
    assert exp_elements[0].attrib['bool_exp'] == 'pvSev0 == 1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pvSev0 == 2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_sevr_options_before_val_options(
        widget, get_opi_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'val_one'), ('2', 'val_two')],
                            sevr_options=[('-1', 'sevr_one'),
                                          ('-2', 'sevr_two')]))

    renderer = get_opi_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 4
    assert exp_elements[0].attrib['bool_exp'] == 'pvSev0 == -1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'sevr_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pvSev0 == -2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'sevr_two'

    assert exp_elements[2].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[2].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[3].attrib['bool_exp'] == 'pv0 == 2'
    value_element = exp_elements[3].find('./value')
    assert value_element.text == 'val_two'


def test_selection_rule_sevr_options_before_val_options_phoebus(
        widget, get_bob_renderer):
    widget.add_rule(
        rules.SelectionRule('test_property',
                            'dummy_pv',
                            val_options=[('1', 'val_one'), ('2', 'val_two')],
                            sevr_options=[('-1', 'sevr_one'),
                                          ('-2', 'sevr_two')]))

    renderer = get_bob_renderer(widget)
    renderer.assemble()
    rule_element = renderer.get_node().find('./rules/rule')
    assert rule_element.find('./pv_name').text == 'dummy_pv'
    assert rule_element.attrib['prop_id'] == 'test_property'
    assert rule_element.attrib['out_exp'] == 'false'

    exp_elements = rule_element.findall('./exp')
    assert len(exp_elements) == 4
    assert exp_elements[0].attrib['bool_exp'] == 'pvSev0 == -1'
    value_element = exp_elements[0].find('./value')
    assert value_element.text == 'sevr_one'

    assert exp_elements[1].attrib['bool_exp'] == 'pvSev0 == -2'
    value_element = exp_elements[1].find('./value')
    assert value_element.text == 'sevr_two'

    assert exp_elements[2].attrib['bool_exp'] == 'pv0 == 1'
    value_element = exp_elements[2].find('./value')
    assert value_element.text == 'val_one'

    assert exp_elements[3].attrib['bool_exp'] == 'pv0 == 2'
    value_element = exp_elements[3].find('./value')
    assert value_element.text == 'val_two'
