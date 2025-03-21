from model.group import Group

def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="test", header="test1", footer="test12"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
