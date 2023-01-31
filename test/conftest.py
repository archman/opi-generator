import pytest

from opigen.opimodel import widgets
from opigen.renderers import css_render
from opigen.renderers import phoebus_render


@pytest.fixture
def widget():
    return widgets.Widget('dummyid', 0, 0, 10, 10)


@pytest.fixture
def display():
    return widgets.Display(100, 100)


@pytest.fixture
def get_opi_renderer():

    def get_renderer(w):
        return css_render.get_opi_renderer(w)

    return get_renderer


@pytest.fixture
def get_bob_renderer():

    def get_renderer(w):
        return phoebus_render.get_opi_renderer(w)

    return get_renderer
