from opigen.opimodel import colors
from opigen.opimodel.borders import Border, BorderStyle

BLACK = colors.Color((0, 0, 0), 'Black')


def test_add_border_to_widget(widget, get_opi_renderer):
    b = Border(BorderStyle.LINE, 1, BLACK, False)
    widget.set_border(b)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    alarm_sensitive = renderer.get_node().find('./border_alarm_sensitive')
    assert alarm_sensitive.text == 'false'
    border_color = renderer.get_node().find('./border_color/color')
    assert border_color.get('red') == '0'
    assert border_color.get('green') == '0'
    assert border_color.get('blue') == '0'
    assert border_color.get('name') == 'Black'
    border_style = renderer.get_node().find('./border_style')
    border_style.text = str(BorderStyle.LINE)
    border_width = renderer.get_node().find('./border_width')
    border_width.text = '1'


def test_add_border_to_widget_phoebus(widget, get_bob_renderer):
    b = Border(BorderStyle.LINE, 1, BLACK, False)
    widget.set_border(b)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    alarm_sensitive = renderer.get_node().find('./border_alarm_sensitive')
    assert alarm_sensitive.text == 'false'
    border_color = renderer.get_node().find('./border_color/color')
    assert border_color.get('red') == '0'
    assert border_color.get('green') == '0'
    assert border_color.get('blue') == '0'
    assert border_color.get('name') == 'Black'
    border_width = renderer.get_node().find('./border_width')
    border_width.text = '1'
    assert renderer.get_node().find('./border_style') is None
