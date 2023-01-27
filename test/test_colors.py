import os
from opigen.opimodel import colors
import pytest
import tempfile


COLOR_FILE_CONTENTS = """
# Alarm colours
Minor = 255, 241, 0
Major = 255, 0, 0
Invalid = 255, 255, 255
Disconnected = 255, 255, 255
# other colors
Button: BG = 205, 205, 205
Related Display: FG = 128, 64, 0
Grey 90% = 230, 230, 230
"""

@pytest.fixture
def color_file():
    tmp = tempfile.NamedTemporaryFile('wt', delete=False)
    tmp.write(COLOR_FILE_CONTENTS)
    tmp.close()
    yield tmp
    os.unlink(tmp.name)


def test_add_color_to_widget(widget, get_opi_renderer):
    c = colors.Color((0, 0, 0), 'black')
    widget.set_fg_color(c)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    fg_color_nodes = renderer.get_node().findall('./foreground_color')
    assert len(fg_color_nodes) == 1
    color_nodes = renderer.get_node().findall('./foreground_color/color')
    assert len(color_nodes) == 1
    assert color_nodes[0].get('red') == '0'
    assert color_nodes[0].get('blue') == '0'
    assert color_nodes[0].get('green') == '0'


def test_add_color_to_widget_phoebus(widget, get_bob_renderer):
    c = colors.Color((0, 0, 0), 'black')
    widget.set_fg_color(c)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    fg_color_nodes = renderer.get_node().findall('./foreground_color')
    assert len(fg_color_nodes) == 1
    color_nodes = renderer.get_node().findall('./foreground_color/color')
    assert len(color_nodes) == 1
    assert color_nodes[0].get('red') == '0'
    assert color_nodes[0].get('blue') == '0'
    assert color_nodes[0].get('green') == '0'


def test_parse_color_file(color_file):
    colors.parse_color_file(color_file.name)

    assert colors.MINOR.red == 255
    assert colors.MINOR.green == 241
    assert colors.MINOR.blue == 0
    assert colors.MINOR.name == 'MINOR'

    assert colors.MAJOR.red == 255
    assert colors.MAJOR.green == 0
    assert colors.MAJOR.blue == 0
    assert colors.MAJOR.name == 'MAJOR'

    assert colors.INVALID.red == 255
    assert colors.INVALID.green == 255
    assert colors.INVALID.blue == 255
    assert colors.INVALID.name == 'INVALID'

    assert colors.DISCONNECTED.red == 255
    assert colors.DISCONNECTED.green == 255
    assert colors.DISCONNECTED.blue == 255
    assert colors.DISCONNECTED.name == 'DISCONNECTED'

    assert colors.BUTTON_BG == colors.Color((205, 205, 205), 'BUTTON_BG')
    assert colors.RELATED_DISPLAY_FG == colors.Color((128, 64, 0), 'RELATED_DISPLAY_FG')
    assert colors.GREY_90_ == colors.Color((230, 230, 230), 'GREY_90_')
