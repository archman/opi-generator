import pytest

from opigen.opimodel import widgets
from opigen.opimodel.colors import Color


def test_widget_attribute_map(widget, get_opi_renderer, get_bob_renderer):
    assert hasattr(widget, 'phoebus_x')
    assert widget.x == widget.phoebus_x
    assert hasattr(widget, 'phoebus_y')
    assert widget.y == widget.phoebus_y
    assert hasattr(widget, 'phoebus_width')
    assert widget.width == widget.phoebus_width
    assert hasattr(widget, 'phoebus_height')
    assert widget.height == widget.phoebus_height
    assert hasattr(widget, 'phoebus_name')
    assert widget.name == widget.phoebus_name


def test_widget_render_contains_correct_values(widget, get_opi_renderer):
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    output = str(renderer)
    assert 'typeId="dummyid"' in output
    assert "<x>0</x>" in output
    assert "<y>0</y>" in output
    assert "<height>10</height>" in output
    assert "<width>10</width>" in output


def test_widget_render_contains_correct_values_phoebus(widget,
                                                       get_bob_renderer):
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    output = str(renderer)
    assert 'type="dummyid"' in output
    assert "<x>0</x>" in output
    assert "<y>0</y>" in output
    assert "<height>10</height>" in output
    assert "<width>10</width>" in output


def test_Display_render_contains_default_values(display, get_opi_renderer):
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>" in output
    assert "<show_grid>true</show_grid>" in output
    assert "<x>0</x>" in output
    assert "<y>0</y>" in output
    assert "<width>100</width>" in output
    assert "<height>100</height>" in output
    assert renderer.get_node().get('version') == display.get_version()


def test_Display_render_contains_default_values_phoebus(
        display, get_bob_renderer):
    renderer = get_bob_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<grid_visible>true</grid_visible>" in output
    assert "<x>0</x>" in output
    assert "<y>0</y>" in output
    assert "<width>100</width>" in output
    assert "<height>100</height>" in output
    assert renderer.get_node().get('version') == display.get_version_phoebus()


def test_Display_render_contains_child_widgets(display, get_opi_renderer):
    renderer = get_opi_renderer(display)
    r = widgets.Rectangle(10, 10, 10, 10)
    display.add_child(r)
    renderer.assemble()
    output = str(renderer)
    assert 'typeId="org.csstudio.opibuilder.widgets.Rectangle"' in output


def test_Display_render_contains_child_widgets_phoebus(display,
                                                       get_bob_renderer):
    renderer = get_bob_renderer(display)
    r = widgets.Rectangle(10, 10, 10, 10)
    display.add_child(r)
    renderer.assemble()
    output = str(renderer)
    assert 'type="rectangle"' in output


def test_Display_render_contains_default_autoscale_options(
        display, get_opi_renderer):
    display.add_scale_options()
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<auto_scale_widgets>" in output
    assert "<min_width>-1</min_width>" in output
    assert "<min_height>-1</min_height>" in output
    assert "<auto_scale_widgets>false</auto_scale_widgets>" in output


def test_Display_render_sets_custom_scale_options(display, get_opi_renderer):
    display.add_scale_options(min_width=10, min_height=20, autoscale=True)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<auto_scale_widgets>" in output
    assert "<min_width>10</min_width>" in output
    assert "<min_height>20</min_height>" in output
    assert "<auto_scale_widgets>true</auto_scale_widgets>" in output


@pytest.mark.parametrize('widget_type,alignbit',
                         [(widgets.TextUpdate, widgets.HA_CENTER),
                          (widgets.TextEntry, widgets.HA_LEFT)])
def test_text_widgets_have_correct_attributes(display, get_opi_renderer,
                                              widget_type, alignbit):
    tb = widget_type(10, 10, 20, 20, 'pvname')
    display.add_child(tb)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>pvname</pv_name>' in output
    assert f'<horizontal_alignment>{alignbit}</horizontal_alignment>' in output


@pytest.mark.parametrize('widget_type,alignbit',
                         [(widgets.TextUpdate, widgets.HA_CENTER),
                          (widgets.TextEntry, widgets.HA_LEFT)])
def test_text_widgets_have_correct_attributes_phoebus(display,
                                                      get_bob_renderer,
                                                      widget_type, alignbit):
    tb = widget_type(10, 10, 20, 20, 'pvname')
    display.add_child(tb)
    renderer = get_bob_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>pvname</pv_name>' in output
    assert f'<horizontal_alignment>{alignbit}</horizontal_alignment>' in output


def test_ToggleButton_has_correct_attributes(display, get_opi_renderer):
    tb = widgets.ToggleButton(10, 10, 20, 20, 'on', 'off')
    display.add_child(tb)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<on_label>on</on_label>' in output
    assert '<off_label>off</off_label>' in output
    assert '<effect_3d>true</effect_3d>' in output


def test_ToggleButton_has_correct_attributes_phoebus(display,
                                                     get_bob_renderer):
    tb = widgets.ToggleButton(10, 10, 20, 20, 'on', 'off')
    display.add_child(tb)
    renderer = get_bob_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<on_label>on</on_label>' in output
    assert '<off_label>off</off_label>' in output


def test_Led_has_correct_attributes(display, get_opi_renderer):
    led = widgets.Led(10, 10, 20, 20, 'TEST')
    display.add_child(led)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output


def test_Led_has_correct_attributes_phoebus(display, get_bob_renderer):
    led = widgets.Led(10, 10, 20, 20, 'TEST')
    display.add_child(led)
    renderer = get_bob_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output


def test_Byte_has_correct_attributes(display, get_opi_renderer):
    byte = widgets.Byte(10, 10, 20, 20, 'TEST', 3)
    display.add_child(byte)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output
    assert '<numBits>3</numBits>' in output
    assert 'startBit' not in output


def test_Byte_has_correct_attributes_phoebus(display, get_bob_renderer):
    byte = widgets.Byte(10, 10, 20, 20, 'TEST', 3)
    display.add_child(byte)
    renderer = get_bob_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output
    assert '<numBits>3</numBits>' in output
    assert 'startBit' not in output


def test_Byte_includes_start_bit_if_specified(display, get_opi_renderer):
    byte = widgets.Byte(10, 10, 20, 20, 'TEST', 3, start_bit=5)
    display.add_child(byte)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output
    assert '<numBits>3</numBits>' in output
    assert '<startBit>5</startBit>' in output


def test_Byte_includes_start_bit_if_specified_phoebus(display,
                                                      get_bob_renderer):
    byte = widgets.Byte(10, 10, 20, 20, 'TEST', 3, start_bit=5)
    display.add_child(byte)
    renderer = get_bob_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<pv_name>TEST</pv_name>' in output
    assert '<numBits>3</numBits>' in output
    assert '<startBit>5</startBit>' in output


def test_Line_has_correct_attributes(display, get_opi_renderer):
    line = widgets.Line(10, 100, 50, 20)
    display.add_child(line)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<x>10</x>' in output
    assert '<y>20</y>' in output
    assert '<points>' in output
    assert '<point x="10" y="100"/>' in output
    assert '<point x="50" y="20"/>' in output


def test_Line_has_correct_attributes_phoebus(display, get_bob_renderer):
    line = widgets.Line(10, 100, 50, 20, 2)
    assert line.x == 10
    assert line.y == 20
    display.add_child(line)
    renderer = get_bob_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<x>10</x>' in output
    assert '<y>20</y>' in output
    assert '<points>' in output
    assert '<point x="0" y="80"/>' in output
    assert '<point x="40" y="0"/>' in output
    assert '<line_width>2</line_width>' in output


def test_ActionWidget_renders_hook_attributes_correctly(
        display, get_opi_renderer):
    aw = widgets.ActionWidget('dummy', 10, 100, 50, 20)
    aw.add_exit()
    display.add_child(aw)
    renderer = get_opi_renderer(display)
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


def test_GroupBox_render_contains_default_autoscale_options(
        display, get_opi_renderer):
    gp = widgets.GroupingContainer(0, 0, 100, 100)
    gp.add_scale_options()
    display.add_child(gp)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<scale_options>" in output
    assert "<width_scalable>true</width_scalable>" in output
    assert "<height_scalable>true</height_scalable>" in output
    assert "<keep_wh_ratio>false</keep_wh_ratio>" in output


def test_GroupBox_render_sets_custom_scale_options(display, get_opi_renderer):
    gp = widgets.GroupingContainer(0, 0, 100, 100)
    gp.add_scale_options(width=False, height=False, keep_wh_ratio=True)
    display.add_child(gp)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert "<scale_options>" in output
    assert "<width_scalable>false</width_scalable>" in output
    assert "<height_scalable>false</height_scalable>" in output
    assert "<keep_wh_ratio>true</keep_wh_ratio>" in output


def test_XYPlot_has_correct_attributes(display, get_opi_renderer):
    xyplot = widgets.XYPlot(10, 10, 20, 20)
    display.add_child(xyplot)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<trace_count>0</trace_count>' in output

    xyplot.add_trace("y_pv", "x_pv", "legend_name", line_width=10)
    renderer.assemble()
    output = str(renderer)
    assert '<trace_count>1</trace_count>' in output
    assert "<trace_0_x_pv>x_pv</trace_0_x_pv>" in output
    assert "<trace_0_y_pv>y_pv</trace_0_y_pv>" in output
    assert "<trace_0_name>legend_name</trace_0_name>" in output


def test_XYPlot_trace_color_works(display, get_opi_renderer):
    xyplot = widgets.XYPlot(10, 10, 20, 20)
    xyplot.add_trace("y_pv",
                     "x_pv",
                     "legend_name",
                     line_width=10,
                     trace_color=Color((255, 0, 0)))
    display.add_child(xyplot)
    renderer = get_opi_renderer(display)
    renderer.assemble()
    output = str(renderer)
    assert '<color red="255" green="0" blue="0"/>' in output
