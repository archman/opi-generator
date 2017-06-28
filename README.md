Simple Python code to generate OPI files for CS-Studio.

[![Build Status](https://travis-ci.org/dls-controls/cssgen.svg?branch=master)](https://travis-ci.org/dls-controls/cssgen)
[![Coverage Status](https://coveralls.io/repos/github/dls-controls/cssgen/badge.svg?branch=master)](https://coveralls.io/github/dls-controls/cssgen?branch=master)
[![Health](https://landscape.io/github/dls-controls/cssgen/master/landscape.svg?style=flat)](https://landscape.io/github/dls-controls/cssgen/master)

## User guide

Assemble an OPI file by creating widgets.  The root widget should be a Display 
object.  Top-level widgets should be added as children of the root widget.  You 
would usually create functions to help create common widgets in your displays.

To write the OPI file out, use a renderer from the renderers package.

### CS-Studio notes

Any public attribute of a widget object will become a sub-element in XML with 
the attribute as tag name.  Any simple XML tag can be created by giving the 
object the correct variable with the correct value.  To find out what attributes
you need, create the widget in CS-Studio and then examine the XML that is 
created when you save the file.

Complicated sub-elements, such as rules and actions, can be created using the
classes in the opimodel package.


## Demo

Examples of the use of the cssgen library are included in the examples folder:
* [Simple example using most features](examples/basic.py) (`examples/basic.py`)


## Developer Guide

To create another type of widget, extend the class `Widget` in 
`opimodel/widgets.py`.

### How to run the tests

Use a virtualenv:

* `virtualenv --no-site-packages venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `export PYTHONPATH=$(pwd)`
* `py.test --cov=renderers --cov=opimodel test`
