import pytest
from cssgen import widgets


@pytest.fixture
def widget():
    return widgets.Widget('dummyid', 0, 0, 10, 10)
