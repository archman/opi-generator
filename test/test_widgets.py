from opigen.opimodel import widgets
import pytest


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


def test_Display_render_contains_default_autoscale_options(display, get_renderer):
    display.add_scale_options()
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<auto_scale_widgets>" in output
    assert "<min_width>-1</min_width>" in output
    assert "<min_height>-1</min_height>" in output
    assert "<auto_scale_widgets>false</auto_scale_widgets>" in output


def test_Display_render_sets_custom_scale_options(display, get_renderer):
    display.add_scale_options(min_width=10, min_height=20, autoscale=True)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<auto_scale_widgets>" in output
    assert "<min_width>10</min_width>" in output
    assert "<min_height>20</min_height>" in output
    assert "<auto_scale_widgets>true</auto_scale_widgets>" in output


@pytest.mark.parametrize('widget_type', (widgets.TextMonitor,
                                         widgets.TextInput))
def test_text_widgets_have_correct_attributes(display, get_renderer, widget_type):
    tb = widget_type(10, 10, 20, 20, 'pvname')
    display.add_child(tb)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>pvname</pv_name>' in output
    assert '<horizontal_alignment>1</horizontal_alignment>' in output


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


def test_ActionWidget_renders_hook_attributes_correctly(display, get_renderer):
    aw = widgets.ActionWidget('dummy', 10, 100, 50, 20)
    aw.add_exit()
    display.add_child(aw)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert 'hook="true"' in output
    assert 'hook_all="false"' in output
    aw.actions.set_hook_all(True)
    renderer.assemble()
    output = str(renderer)
    assert 'hook="true"' in output
    assert 'hook_all="true"' in output
    aw.actions.set_hook_first(False)
    renderer.assemble()
    output = str(renderer)
    assert 'hook="false"' in output
    assert 'hook_all="true"' in output


def test_ToggleButton_adds_actions_correctly():
    tb = widgets.ToggleButton(0, 0, 10, 10, 'on', 'off')
    tb.add_push_action('dummy1')
    assert len(tb.actions) == 1
    assert tb.actions[0] == 'dummy1'
    assert tb.push_action_index == 0
    assert tb.released_action_index != 0
    tb.add_release_action('dummy2')
    assert len(tb.actions) == 2
    assert tb.actions[1] == 'dummy2'
    assert tb.released_action_index == 1
    assert tb.actions.get_hook_first() is True
    assert tb.actions.get_hook_all() is False


def test_GroupBox_render_contains_default_autoscale_options(display, get_renderer):
    gp = widgets.GroupingContainer(0, 0, 100, 100)
    gp.add_scale_options()
    display.add_child(gp)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<scale_options>" in output
    assert "<width_scalable>true</width_scalable>" in output
    assert "<height_scalable>true</height_scalable>" in output
    assert "<keep_wh_ratio>false</keep_wh_ratio>" in output


def test_GroupBox_render_sets_custom_scale_options(display, get_renderer):
    gp = widgets.GroupingContainer(0, 0, 100, 100)
    gp.add_scale_options(width=False, height=False, keep_wh_ratio=True)
    display.add_child(gp)
    renderer = get_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<scale_options>" in output
    assert "<width_scalable>false</width_scalable>" in output
    assert "<height_scalable>false</height_scalable>" in output
    assert "<keep_wh_ratio>true</keep_wh_ratio>" in output
