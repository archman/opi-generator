from opimodel import borders, colors


BLACK = colors.Color((0, 0, 0), 'Black')

def test_add_border_to_widget(widget, get_renderer):
    b = borders.Border(borders.LINE_STYLE, 1, BLACK, False)
    widget.set_border(b)
    renderer = get_renderer(widget)
    renderer.assemble()
    alarm_sensitive = renderer.get_node().find('./border_alarm_sensitive')
    assert alarm_sensitive.text == 'false'
    border_color = renderer.get_node().find('./border_color/color')
    assert border_color.get('red') == '0'
    assert border_color.get('green') == '0'
    assert border_color.get('blue') == '0'
    assert border_color.get('name') == 'Black'
