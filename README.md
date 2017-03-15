Simple Python code to generate OPI files for CS-Studio.

[![Build Status](https://travis-ci.org/willrogers/cssgen.svg?branch=master)](https://travis-ci.org/willrogers/cssgen)
[![Coverage Status](https://coveralls.io/repos/github/willrogers/cssgen/badge.svg?branch=master)](https://coveralls.io/github/willrogers/cssgen?branch=master)


## How it works

Assemble an OPI file by creating widgets.  The root widget should be a Display.  It should have top-level widgets as children.

Properties of widgets are called nodes.  Any attribute of a widget object should inherit from Node and will become a sub-element in XML.  A sub-element with multiple children, such as rules and actions, should be a ParentNode that contains a list of the appropriate nodes.

## Demo

    from cssgen import widgets, nodes, actions, rules

    # Create the root widget.
    d = widgets.Display(200, 200)
    # Add a rectangle.
    rect = widgets.Rectangle(10, 10, 10, 10)
    d.add_child(rect)
    # Add a grouping container.
    group = widgets.GroupingContainer(30, 30, 90, 90)
    d.add_child(group)
    # Add two action buttons to the grouping container.
    ab = actions.ActionButton(30, 30, 30, 30, 'hello')
    group.add_child(ab)
    ab.add_write_pv('helo', 'bye')
    ab2 = actions.ActionButton(60, 60, 60, 60, 'ls')
    ab2.add_shell_command('ls')
    group.add_child(ab2)
    # Add a rule to the grouping container.
    group.rules = nodes.ListNode()
    group.rules.add_child(rules.GreaterThanRuleNode('visible', 'SR-CS-FILL-01:COUNTDOWN', 300))
    # Write the OPI file.
    d.write_to_file('demo.opi')

## How to run the tests

Use a virtualenv:

* `virtualenv --no-site-packages venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `py.test --cov=cssgen test`
