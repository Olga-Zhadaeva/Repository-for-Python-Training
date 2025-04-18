from random import randrange
from model.group import Group

def test_edit_first_group_full(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="1test", header="2test", footer="12test")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
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
