import pytest

from utils import widget
from cssgen import actions, widgets


def test_ActionButton_adds_shell_command(widget):
    ab = actions.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_shell_command('ls')
    widget.assemble()
    action_nodes = ab.get_node().findall('./actions/action')
    assert action_nodes[0].find('./command').text == 'ls'
    assert action_nodes[0].find('./command_directory').text == '$(opi.dir)'


def test_ActionButton_adds_write_pv(widget):
    ab = actions.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_write_pv('hello', 'bye')
    widget.assemble()
    action_nodes = ab.get_node().findall('./actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].find('./pv_name').text == 'hello'
    assert action_nodes[0].find('./value').text == 'bye'
