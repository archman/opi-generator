import pytest

from opigen.opimodel import widgets
from opigen.renderers.css import render


@pytest.fixture
def widget():
    return widgets.Widget('dummyid', 0, 0, 10, 10)


@pytest.fixture
def display():
    return widgets.Display(100, 100)


@pytest.fixture
def get_renderer():
    def get_renderer(w):
        return render.get_opi_renderer(w)

    return get_renderer
