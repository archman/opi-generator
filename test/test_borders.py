from opimodel import widgets, borders, colors


def test_add_border_to_widget(widget, get_renderer):
    w = widgets.Widget('dummy', 0, 0, 0, 0)
    b = borders.Border(borders.LINE_STYLE, 1, colors.BLACK, False)
    w.set_border(b)
    renderer = get_renderer(w)
    renderer.assemble()
    alarm_sensitive = renderer.get_node().find('./border_alarm_sensitive')
    assert alarm_sensitive.text == 'false'
    border_color = renderer.get_node().find('./border_color/color')
    assert border_color.get('red') == '0'
    assert border_color.get('green') == '0'
    assert border_color.get('blue') == '0'
    assert border_color.get('name') == 'Black'
