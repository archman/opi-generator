import pytest
from utils import widget
from cssgen import nodes


def test_widget_render_contains_dynamically_added_values(widget):
    widget.test = nodes.TextNode('dummy')
    output = str(widget)
    assert '<test>dummy</test>' in output
