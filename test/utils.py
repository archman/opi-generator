import pytest
from model import widgets
from cssgen import render, actions, rules


@pytest.fixture
def widget():
    return widgets.Widget('dummyid', 0, 0, 10, 10)


@pytest.fixture
def display():
    return widgets.Display(100, 100)


@pytest.fixture
def get_renderer():
    def get_renderer(w):
        ar = actions.OpiActionRenderer()
        rr = rules.OpiRuleRenderer()
        tr = render.OpiTextRenderer()
        return render.OpiRenderer(w, render.OpiWidgetRenderer(ar, rr, tr))
    return get_renderer
