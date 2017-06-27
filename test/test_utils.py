from opimodel import utils
import pytest


@pytest.mark.parametrize('input,output',
                         [('hello', 'HELLO'),
                          ('Hello:', 'HELLO_'),
                          ('Hello: Goodbye', 'HELLO_GOODBYE'),
                          ('Dummy 1', 'DUMMY_1')])
def test_mangle_name_handles_various_cases(input, output):
    assert utils.mangle_name(input) == output
