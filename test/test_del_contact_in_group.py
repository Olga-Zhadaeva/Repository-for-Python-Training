from model.contact import Contact
from model.group import Group
import random

def test_del_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name='test'))

    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya", title="1Man", company="1unreal", address="1Moscow", home="1St. Petersburg",
                            mobile="188888888888", work="189888888888", fax="189988888888", email="1Ivan@gmail.com", email2="1Ivan@mail.ru",
                            email3="1Iban@yandex.ru", homepage="1something", bday="2", bmonth="February", byear="2002", aday="3", amonth="March", ayear="2003"))

    groups = orm.get_group_list()
    contact_in_group = []
    for group in groups:
        contacts_in_group = orm.get_contacts_in_group(group)
        if contacts_in_group:
            contact = random.choice(contacts_in_group)
            contact_in_group.append((contact, group))

    if not contact_in_group:
        contact = random.choice(orm.get_contact_list())
        group = random.choice(groups)
        app.contact.add_contact_in_group(contact.id, group.id)
        contact_in_group.append((contact, group))

    contact, group = random.choice(contact_in_group)
    app.contact.delete_contact_in_group(contact.id, group.id)

    contact_not_group = orm.get_contacts_not_in_group(group)
    assert contact.id in [c.id for c in contact_not_group]
