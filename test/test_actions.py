import pytest

from utils import widget, get_renderer
from model import widgets
from cssgen import actions, render


def test_ActionButton_adds_shell_command(widget, get_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_shell_command('ls')
    renderer = get_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert action_nodes[0].find('./command').text == 'ls'
    assert action_nodes[0].find('./command_directory').text == '$(opi.dir)'


def test_ActionButton_adds_write_pv(widget, get_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_write_pv('hello', 'bye')
    renderer = get_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].find('./pv_name').text == 'hello'
    assert action_nodes[0].find('./value').text == 'bye'
