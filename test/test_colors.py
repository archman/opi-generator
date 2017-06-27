from opimodel import colors
import mock
import sys

# Python 2 and 3 compatibility
OPEN_FN_NAME = ('__builtin__.open'
                if sys.version_info.major == 2
                else 'builtins.open')

COLOR_FILE_CONTENTS = """
# Alarm colours
Minor = 255, 241, 0
Major = 255, 0, 0
Invalid = 255, 255, 255
Disconnected = 255, 255, 255
"""


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


def test_parse_css_color_file():
    mock_open = mock.mock_open(read_data=COLOR_FILE_CONTENTS)
    with mock.patch(OPEN_FN_NAME, mock_open) as mock_file:
        colors.parse_css_color_file(mock_file)
        assert colors.MINOR.red == 255
        assert colors.MAJOR.green == 0
        assert colors.INVALID.green == 255
        assert colors.DISCONNECTED.name == 'Disconnected'
