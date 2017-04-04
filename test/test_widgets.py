import pytest
from model import widgets
from cssgen import render, rules, actions


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
