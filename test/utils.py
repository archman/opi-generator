import pytest
from model import widgets


@pytest.fixture
def widget():
    return widgets.WidgetModel('dummyid', 0, 0, 10, 10)
