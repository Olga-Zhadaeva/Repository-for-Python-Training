import pytest
from group import Group
from training.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group(name="test", header="test1", footer="test12"))
    app.logout()


def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
