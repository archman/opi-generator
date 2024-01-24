import os
import tempfile

import pytest

from opigen.opimodel import fonts

TEST_FONT_FILE = """dummy 1 = Dummy one-bold-19pt
dummy 2 = Dummy two-italic-15px
dummy 3 = Dummy one-regular-14
// comment line 1
# comment line 2
# do not trim the trailing spaces in the next line!
dummy 4  =  another dummy font family  - regular  - 20  
# define size for phoebus
dummy 5 = Font name contains no digit - bold - 14pt, 24
"""


@pytest.fixture
def font_file():
    tmp = tempfile.NamedTemporaryFile('wt', delete=False)
    tmp.write(TEST_FONT_FILE)
    tmp.close()
    yield tmp
    os.unlink(tmp.name)


def test_add_font_to_widget(widget, get_opi_renderer):
    f = fonts.Font(name='Dummy Font Name',
                   fontface='Dummy Font Face',
                   size=12,
                   style=fonts.REGULAR)
    widget.set_font(f)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    node = renderer.get_node()
    font_nodes = node.findall('./font')
    assert len(font_nodes) == 1
    fontdata_nodes = node.findall('./font/fontdata')
    assert len(fontdata_nodes) == 1
    assert fontdata_nodes[0].text == 'Dummy Font Name'
    assert fontdata_nodes[0].get('fontName') == 'Dummy Font Face'
    assert fontdata_nodes[0].get('height') == '12'
    assert fontdata_nodes[0].get('style') == '0'
    assert fontdata_nodes[0].get('pixels') == 'true'
    # renderer.write_to_file('/tmp/test.opi')


def test_add_font_to_widget_phoebus(widget, get_bob_renderer):
    f = fonts.Font(name='Dummy Font Name',
                   fontface='Dummy Font Face',
                   size=12,
                   style=fonts.REGULAR)
    widget.set_font(f)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    node = renderer.get_node()
    font_nodes = node.findall('./font')
    assert len(font_nodes) == 1
    fontdata_nodes = node.findall('./font/font')
    assert len(fontdata_nodes) == 1
    assert fontdata_nodes[0].text == 'Dummy Font Name'
    assert fontdata_nodes[0].get('family') == 'Dummy Font Face'
    assert fontdata_nodes[0].get('size') == '12'
    assert fontdata_nodes[0].get('style') == 'REGULAR'


def test_parse_font_file(font_file):
    fonts.parse_font_file(font_file.name)
    assert fonts.DUMMY_1 == fonts.Font('dummy 1',
                                       'Dummy one',
                                       19,
                                       fonts.BOLD,
                                       pixels=False,
                                       phoebus_size=19)
    assert fonts.DUMMY_1.name == 'dummy 1'
    assert fonts.DUMMY_1.fontface == 'Dummy one'
    assert fonts.DUMMY_1.style == fonts.BOLD
    assert fonts.DUMMY_1.style_as_str() == 'BOLD'
    assert fonts.DUMMY_1.size == 19
    assert fonts.DUMMY_1.phoebus_size == 19
    assert not fonts.DUMMY_1.pixels
    assert fonts.DUMMY_2 == fonts.Font('dummy 2',
                                       'Dummy two',
                                       15,
                                       fonts.ITALIC,
                                       pixels=True,
                                       phoebus_size=15)
    assert fonts.DUMMY_3 == fonts.Font('dummy 3',
                                       'Dummy one',
                                       14,
                                       fonts.REGULAR,
                                       pixels=True,
                                       phoebus_size=14)
    assert fonts.DUMMY_4 == fonts.Font('dummy 4',
                                       'another dummy font family',
                                       20,
                                       fonts.REGULAR,
                                       pixels=True,
                                       phoebus_size=20)
    assert fonts.DUMMY_5 == fonts.Font('dummy 5',
                                       'Font name contains no digit',
                                       14,
                                       fonts.BOLD,
                                       pixels=False,
                                       phoebus_size=24)
