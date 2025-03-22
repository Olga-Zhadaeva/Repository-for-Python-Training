from model.group import Group

def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="1test", header="2test", footer="12test"))
    app.session.logout()