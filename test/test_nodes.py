import pytest
from cssgen import nodes
from cssgen import widgets


@pytest.fixture
def widget():
    return widgets.Widget('dummyid', 0, 0, 10, 10)


def test_widget_render_contains_dynamically_added_values(widget):
    widget.test = nodes.TextNode('dummy')
    output = str(widget)
    assert "<test>dummy</test>" in output
