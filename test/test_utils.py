from opigen.opimodel import utils
import pytest
import sys


@pytest.mark.parametrize('raw,mangled', [('hello', 'HELLO'),
                                         ('Hello:', 'HELLO_'),
                                         ('Hello: Goodbye', 'HELLO_GOODBYE'),
                                         ('Dummy 1', 'DUMMY_1')])
def test_mangle_name_handles_various_cases(raw, mangled):
    assert utils.mangle_name(raw) == mangled


def test_add_attr_to_module():
    # Add the variable x to the current module with value 1
    utils.add_attr_to_module('x', 1, sys.modules[__name__])
    # We expect pylint to complain about this.
    assert X == 1 # noqa: F821 #pylint: disable=undefined-variable
