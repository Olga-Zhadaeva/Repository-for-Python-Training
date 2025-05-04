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

    groups = orm.get_group_list()
    all_contacts = orm.get_contact_list()
    all_contacts_in_group = []
    group_for_add = random.choice(groups)
    contact_for_add = None

    for group in groups:
        all_contacts_in_group.extend(orm.get_contacts_in_group(group))

    for contact in all_contacts:
        if contact not in all_contacts_in_group:
            contact_for_add = contact
            break

    if contact_for_add is None:
        app.contact.create(Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya"))
        contact_for_add = orm.get_contact_list()[-1]

    app.contact.add_contact_in_group(contact_for_add.id, group_for_add.id)
    contacts_in_group = orm.get_contacts_in_group(group_for_add)
    assert contact_for_add.id in [c.id for c in contacts_in_group]