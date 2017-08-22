from opimodel import widgets


def test_widget_render_contains_correct_values(widget, get_renderer):
    renderer = get_renderer(widget)
    renderer.assemble()
    output = str(renderer)
    assert 'typeId="dummyid"' in output
    assert "<x>0</x>" in output
    assert "<y>0</y>" in output
    assert "<height>10</height>" in output
    assert "<width>10</width>" in output


def test_Display_render_contains_default_values(display, get_renderer):
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>" in output


def test_Display_render_contains_child_widgets(display, get_renderer):
    renderer = get_renderer(display)
    r = widgets.Rectangle(10, 10, 10, 10)
    display.add_child(r)
    renderer.assemble()
    output = str(renderer)
    assert 'typeId="org.csstudio.opibuilder.widgets.Rectangle"' in output


def test_ToggleButton_has_correct_attributes(display, get_renderer):
    tb = widgets.ToggleButton(10, 10, 20, 20, 'on', 'off')
    display.add_child(tb)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<on_label>on</on_label>' in output
    assert '<off_label>off</off_label>' in output
    assert '<effect_3d>true</effect_3d>' in output


def test_Led_has_correct_attributes(display, get_renderer):
    led = widgets.Led(10, 10, 20, 20, 'TEST')
    display.add_child(led)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output


def test_Byte_has_correct_attributes(display, get_renderer):
    byte = widgets.Byte(10, 10, 20, 20, 'TEST', 3)
    display.add_child(byte)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output
    assert '<numBits>3</numBits>' in output
    assert 'startBit' not in output

def test_Byte_includes_start_bit_if_specified(display, get_renderer):
    byte = widgets.Byte(10, 10, 20, 20, 'TEST', 3, start_bit=5)
    display.add_child(byte)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output
    assert '<numBits>3</numBits>' in output
    assert '<startBit>5</startBit>' in output

def test_Line_has_correct_attributes(display, get_renderer):
    byte = widgets.Line(10, 100, 50, 20)
    display.add_child(byte)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<x>10</x>' in output
    assert '<y>20</y>' in output
    assert '<points>' in output
    assert '<point x="10" y="100"/>' in output
    assert '<point x="50" y="20"/>' in output
