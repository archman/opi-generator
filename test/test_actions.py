from opimodel import actions, widgets
import pytest


@pytest.mark.parametrize('n', [0, 1, 2, 3])
def test_adding_action_n_times_results_in_n_actions(widget, get_renderer, n):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    command = actions.ExecuteCommand('ls', 'list directory')
    widget.add_child(ab)
    # Add the action n times.  Note that adding the same action twice does
    # result in more than one action being included in the opi.
    for i in range(n):
        ab.add_action(command)
    renderer = get_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == n
    for i in range(n):
        assert action_nodes[i].find('./command').text == 'ls'
        assert action_nodes[i].find('./command_directory').text == '$(opi.dir)'


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


def test_ActionButton_adds_open_opi_action(widget, get_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_open_opi('file/path', mode=42)
    renderer = get_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].find('./path').text == 'file/path'
    assert action_nodes[0].find('./mode').text == '42'
