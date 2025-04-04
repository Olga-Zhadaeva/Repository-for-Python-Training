from model.group import Group

def test_edit_first_group_full(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name="1test", header="2test", footer="12test"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name="New group"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(header="New header"))
