from opimodel import fonts


def test_add_font_to_widget(widget, get_renderer):
    f = fonts.Font('Dummy name', 12, fonts.REGULAR)
    widget.set_font(f)
    renderer = get_renderer(widget)
    renderer.assemble()
    node = renderer.get_node()
    font_nodes = node.findall('./font')
    assert len(font_nodes) == 1
    opifont_nodes = node.findall('./font/opifont.name')
    assert len(opifont_nodes) == 1
    assert opifont_nodes[0].get('fontName') == 'Dummy name'
    assert opifont_nodes[0].get('height') == '12'
    assert opifont_nodes[0].get('style') == '0'
