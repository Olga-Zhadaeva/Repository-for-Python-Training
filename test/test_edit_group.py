from model.group import Group

def test_edit_first_group_full(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="1test", header="2test", footer="12test"))
    app.session.logout()

def test_edit_first_group_name(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="New group"))
    app.session.logout()

def test_edit_first_group_header(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(header="New header"))
    app.session.logout()
