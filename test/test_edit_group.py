import random
from model.group import Group

def test_edit_first_group_full(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new_data = Group(name="1test", header="2test", footer="12test")
    app.group.edit_group_by_id(group.id, group_new_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group_new_data.id = group.id
    old_groups = [g if g.id != group.id else group_new_data for g in old_groups]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
#
# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="New group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_edit_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
