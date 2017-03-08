import pytest
import widgets


@pytest.fixture
def widget():
    return widgets.Widget('dummyid', 0, 0, 10, 10)


@pytest.fixture
def display():
    return widgets.Display(100, 100)


def test_widget_render_contains_correct_values(widget):
    output = str(widget)
    assert 'typeId="dummyid"' in output
    assert "<x>0</x>" in output
    assert "<y>0</y>" in output
    assert "<height>10</height>" in output
    assert "<width>10</width>" in output


def test_widget_render_contains_dynamically_added_values(widget):
    widget.test = 'dummy'
    output = str(widget)
    assert "<test>dummy</test>" in output


def test_Display_render_contains_default_values(display):
    output = str(display)
    assert "<auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>" in output


def test_Display_render_contains_child_widgets(display):
    widgets.Rectangle(10, 10, 10, 10, display)
    output = str(display)
    assert 'typeId="org.csstudio.opibuilder.widgets.Rectangle"' in output
