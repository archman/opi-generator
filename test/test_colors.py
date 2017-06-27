from opimodel import colors


def test_add_color_to_widget(widget, get_renderer):
    c = colors.Color((0, 0, 0), 'black')
    widget.set_fg_color(c)
    renderer = get_renderer(widget)
    renderer.assemble()
    fg_color_nodes = renderer.get_node().findall('./foreground_color')
    assert len(fg_color_nodes) == 1
    color_nodes = renderer.get_node().findall('./foreground_color/color')
    assert len(color_nodes) == 1
    assert color_nodes[0].get('red') == '0'
    assert color_nodes[0].get('blue') == '0'
    assert color_nodes[0].get('green') == '0'
