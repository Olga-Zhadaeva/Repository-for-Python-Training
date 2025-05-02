from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name='test'))

    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya", title="1Man", company="1unreal", address="1Moscow", home="1St. Petersburg",
                            mobile="188888888888", work="189888888888", fax="189988888888", email="1Ivan@gmail.com", email2="1Ivan@mail.ru",
                            email3="1Iban@yandex.ru", homepage="1something", bday="2", bmonth="February", byear="2002", aday="3", amonth="March", ayear="2003"))

    list_groups_ui = app.group.get_group_list()
    list_contacts_ui = app.contact.get_contact_list()

    group = random.choice(list_groups_ui)
    contact = random.choice(list_contacts_ui)
    app.contact.add_contact_in_group(contact.id, group.id)

    contact_in_group = orm.get_contacts_in_group(group)
    assert contact.id in [c.id for c in contact_in_group]