Simple Python code to generate OPI files for CS-Studio.

[![Build Status](https://travis-ci.org/willrogers/cssgen.svg?branch=master)](https://travis-ci.org/willrogers/cssgen)
[![Coverage Status](https://coveralls.io/repos/github/willrogers/cssgen/badge.svg?branch=master)](https://coveralls.io/github/willrogers/cssgen?branch=master)


## How it works

Assemble an OPI file by creating widgets.  The root widget should be a Display object.  Top-level widgets should be added as children of the root widget.

Any public attribute of a widget object will become a sub-element in XML with the attribute as tag name.  Complicated sub-elements, such as rules and actions, can be created using the classes in the opimodel package.

To write the OPI file out, use the renderers in the cssgen package.

## Demo

    from opimodel import widgets, nodes, actions, rules
    from cssgen import render

    # Create the root widget
    d = widgets.Display(100, 100)
    # Add a rectangle.
    w = widgets.Rectangle(0, 0, 10, 10)
    d.add_child(w)
    # Add a grouping container.
    group = widgets.GroupingContainer(30, 30, 90, 90)
    # Add two action buttons to the grouping container.
    ab = widgets.ActionButton(30, 30, 30, 30, 'hello')
    ab.add_write_pv('hello', 'bye')
    group.add_child(ab)
    ab2 = widgets.ActionButton(60, 60, 60, 60, 'ls')
    ab2.add_shell_command('ls')
    group.add_child(ab2)
    # Add a rule to the grouping container.
    group.rules = []
    group.rules.append(rules.GreaterThanRule('visible', 'SR-CS-FILL-01:COUNTDOWN', 300))
    d.add_child(group)

    # Write the OPI file.
    o = render.get_opi_renderer(d)
    o.write_to_file(name)

## How to run the tests

Use a virtualenv:

* `virtualenv --no-site-packages venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `py.test --cov=cssgen --cov=opimodel test`
