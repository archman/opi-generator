from opigen import actions, widgets
import pytest


def test_ActionsModel_obeys_sequence_protocol():
    a = actions.ActionsModel()
    assert len(a) == 0
    assert not a
    a.add_action('dummy')
    assert len(a) == 1
    assert a
    assert a[0] == 'dummy'


def test_widget_with_no_actions_does_not_have_an_actions_node(
        widget, get_opi_renderer):
    aw = widgets.ActionWidget('dummy_id', 0, 0, 0, 0)
    assert len(aw.actions) == 0
    widget.add_child(aw)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    actions_nodes = renderer.get_node().findall('./widget/actions')
    assert len(actions_nodes) == 0


def test_widget_with_no_actions_does_not_have_an_actions_node_phoebus(
        widget, get_bob_renderer):
    aw = widgets.ActionWidget('dummy_id', 0, 0, 0, 0)
    assert len(aw.actions) == 0
    widget.add_child(aw)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    actions_nodes = renderer.get_node().findall('./widget/actions')
    assert len(actions_nodes) == 0


@pytest.mark.parametrize('n', [0, 1, 2, 3])
def test_adding_action_n_times_results_in_n_actions(widget, get_opi_renderer,
                                                    n):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    command = actions.ExecuteCommand('ls', 'list directory')
    widget.add_child(ab)
    # Add the action n times.  Note that adding the same action twice does
    # result in more than one action being included in the opi.
    for i in range(n):
        ab.add_action(command)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == n
    for i in range(n):
        assert action_nodes[i].find('./command').text == 'ls'
        assert action_nodes[i].find('./command_directory').text == '$(opi.dir)'


@pytest.mark.parametrize('n', [0, 1, 2, 3])
def test_adding_action_n_times_results_in_n_actions_phoebus(
        widget, get_bob_renderer, n):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    command = actions.ExecuteCommand('ls', 'list directory')
    widget.add_child(ab)
    # Add the action n times.  Note that adding the same action twice does
    # result in more than one action being included in the opi.
    for i in range(n):
        ab.add_action(command)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == n
    for i in range(n):
        assert action_nodes[i].find('./command').text == 'ls'
        assert action_nodes[i].find('./description').text == 'list directory'


def test_ActionButton_adds_shell_command(widget, get_opi_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_shell_command('ls')
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert action_nodes[0].get('type') == 'EXECUTE_CMD'
    assert action_nodes[0].find('./command').text == 'ls'
    assert action_nodes[0].find('./command_directory').text == '$(opi.dir)'


def test_ActionButton_adds_shell_command_phoebus(widget, get_bob_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_shell_command('ls')
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert action_nodes[0].get('type') == 'command'
    assert action_nodes[0].find('./command').text == 'ls'
    assert action_nodes[0].find('./command_directory') is None


def test_ActionButton_adds_write_pv(widget, get_opi_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_write_pv('hello', 'bye')
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].get('type') == 'WRITE_PV'
    assert action_nodes[0].find('./pv_name').text == 'hello'
    assert action_nodes[0].find('./value').text == 'bye'


def test_ActionButton_adds_write_pv_phoebus(widget, get_bob_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_write_pv('hello', 'bye', "Write pv 'hello' with 'bye'")
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].get('type') == 'write_pv'
    assert action_nodes[0].find('./pv_name').text == 'hello'
    assert action_nodes[0].find('./value').text == 'bye'
    assert action_nodes[0].find(
        './description').text == "Write pv 'hello' with 'bye'"


def test_ActionButton_adds_open_opi_action(widget, get_opi_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_open_opi('file/path', mode=42)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].get('type') == 'OPEN_DISPLAY'
    assert action_nodes[0].find('./path').text == 'file/path'
    assert action_nodes[0].find('./mode').text == '42'


def test_ActionButton_adds_open_opi_action_phoebus(widget, get_bob_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    widget.add_child(ab)
    ab.add_open_opi('file/path', mode=1)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].get('type') == 'open_display'
    assert action_nodes[0].find('./file').text == 'file/path'
    assert action_nodes[0].find('./target').text == 'tab'


@pytest.mark.parametrize('parent_macros', (True, False))
@pytest.mark.parametrize('macros', ({'a': 'b'}, None))
def test_ActionButton_adds_open_opi_action_with_macros(widget,
                                                       get_opi_renderer,
                                                       macros, parent_macros):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    ab.add_open_opi('file/path',
                    mode=42,
                    macros=macros,
                    parent_macros=parent_macros)
    widget.add_child(ab)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    macros_node = renderer.get_node().findall(
        './widget/actions/action/macros')[0]
    parent_macros_expected = 'true' if parent_macros else 'false'
    assert macros_node.find(
        'include_parent_macros').text == parent_macros_expected
    if macros:
        for m in macros:
            assert macros_node.find(m).text == macros[m]


@pytest.mark.parametrize('macros', ({'a': 'b'}, None))
def test_ActionButton_adds_open_opi_action_with_macros_phoebus(
        widget, get_bob_renderer, macros):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    ab.add_open_opi('file/path', mode=42, macros=macros)
    widget.add_child(ab)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    macros_node = renderer.get_node().findall(
        './widget/actions/action/macros')[0]
    if macros:
        for m in macros:
            assert macros_node.find(m).text == macros[m]


@pytest.mark.parametrize(
    'macros,raise_expected',
    (
        ({
            'a': 'b'
        }, False),
        ({
            'a': 10
        }, False),
        ({
            10: 'a'
        }, True),  # key not a string
        ({
            10: 11
        }, True),  # key not a string
        ({
            'a b': 11
        }, True),  # space in key
        ({
            '1': 'a'
        }, True)))  # key begins with number
def test_ActionButton_open_opi_macros_raise_ValueError_if_macros_not_strings(
        widget, get_opi_renderer, macros, raise_expected):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    ab.add_open_opi('file/path', mode=42, macros=macros)
    widget.add_child(ab)
    renderer = get_opi_renderer(widget)
    if raise_expected:
        with pytest.raises(ValueError):
            renderer.assemble()
    else:
        renderer.assemble()


@pytest.mark.parametrize(
    'macros,raise_expected',
    (
        ({
            'a': 'b'
        }, False),
        ({
            'a': 10
        }, False),
        ({
            10: 'a'
        }, True),  # key not a string
        ({
            10: 11
        }, True),  # key not a string
        ({
            'a b': 11
        }, True),  # space in key
        ({
            '1': 'a'
        }, True)))  # key begins with number
def test_ActionButton_open_opi_macros_raise_ValueError_if_macros_not_strings_phoebus(
        widget, get_bob_renderer, macros, raise_expected):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    ab.add_open_opi('file/path', mode=42, macros=macros)
    widget.add_child(ab)
    renderer = get_bob_renderer(widget)
    if raise_expected:
        with pytest.raises(ValueError):
            renderer.assemble()
    else:
        renderer.assemble()


def test_ActionButton_adds_exit_action(widget, get_opi_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    ab.add_exit()
    widget.add_child(ab)
    renderer = get_opi_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].get('type') == 'EXECUTE_JAVASCRIPT'
    assert action_nodes[0].find('./embedded').text == 'true'


def test_ActionButton_adds_exit_action_phoebus(widget, get_bob_renderer):
    ab = widgets.ActionButton(0, 0, 0, 0, 'dummy')
    ab.add_exit()
    widget.add_child(ab)
    renderer = get_bob_renderer(widget)
    renderer.assemble()
    action_nodes = renderer.get_node().findall('./widget/actions/action')
    assert len(action_nodes) == 1
    assert action_nodes[0].get('type') == 'execute'
    assert action_nodes[0].find('./script').get('file') == 'EmbeddedJs'
    assert action_nodes[0].find('./description').text == 'Exit'
