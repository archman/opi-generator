import pytest

from cssgen import actions, widgets


@pytest.fixture
def root_widget():
    return widgets.Widget('dummyid', 0, 0, 0, 0, None)


def test_ActionButton_adds_shell_command(root_widget):
    ab = actions.ActionButton(0, 0, 0, 0, 'dummy')
    root_widget.add_child(ab)
    ab.add_shell_command('ls')
    root_widget.assemble()
    action_nodes = ab.get_node().findall('./actions/action')
    assert action_nodes[0].find('./command').text == 'ls'
    assert action_nodes[0].find('./command_directory').text == '$(opi.dir)'


def test_ActionButton_adds_write_pv(root_widget):
    ab = actions.ActionButton(0, 0, 0, 0, 'dummy')
    root_widget.add_child(ab)
    ab.add_write_pv('hello', 'bye')
    root_widget.assemble()
    action_nodes = ab.get_node().findall('./actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].find('./pv_name').text == 'hello'
    assert action_nodes[0].find('./value').text == 'bye'
