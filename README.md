Simple Python code to generate OPI files for CS-Studio.

[![Build Status](https://travis-ci.org/dls-controls/cssgen.svg?branch=master)](https://travis-ci.org/dls-controls/cssgen)
[![Coverage Status](https://coveralls.io/repos/github/dls-controls/cssgen/badge.svg?branch=master)](https://coveralls.io/github/dls-controls/cssgen?branch=master)
[![Health](https://landscape.io/github/dls-controls/cssgen/master/landscape.svg?style=flat)](https://landscape.io/github/dls-controls/cssgen/master)

## User guide

Assemble an OPI file by creating widgets.  The root widget should be a Display object.  Top-level widgets should be added as children of the root widget.  You would usually create functions to help create common widgets in your displays.

To write the OPI file out, use a renderer from the renderers package.

### CS-Studio notes

Any public attribute of a widget object will become a sub-element in XML with the attribute as tag name.  Any simple XML tag can be created by giving the object the correct variable with the correct value.  To find out what attributes you need, create the widget in CS-Studio and then examine the XML that is created when you save the file.

Complicated sub-elements, such as rules and actions, can be created using the classes in the opimodel package.


## Demo
    from opimodel import colors, fonts, rules, widgets
    from renderers.css import render

    # Read the color and font data from the
    colors.parse_css_color_file('color.def')
    fonts.parse_css_font_file('font.def')

    # Create the root widget
    d = widgets.Display(100, 100)
    # Add a rectangle.
    w = widgets.Rectangle(0, 0, 10, 10)
    w.set_fg_color(colors.YELLOW_LED_OFF)
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
    group.rules.append(
        rules.GreaterThanRule('visible', 'SR-CS-FILL-01:COUNTDOWN', 300))
    d.add_child(group)

    # Add a label with fonts and colour from the config files
    l = widgets.Label(100, 100, 200, 20, "test_label")
    l.set_font(fonts.FINE_PRINT)
    d.add_child(l)

    # Write the OPI file.
    o = render.get_opi_renderer(d)
    o.write_to_file(filename)


## Developer Guide

To create another type of widget, extend the class `Widget` in `opimodel/widgets.py`.

### How to run the tests

Use a virtualenv:

* `virtualenv --no-site-packages venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `export PYTHONPATH=$(pwd)`
* `py.test --cov=renderers --cov=opimodel test`
