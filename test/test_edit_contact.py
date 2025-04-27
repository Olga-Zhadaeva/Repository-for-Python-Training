from model.contact import Contact
import random

def test_edit_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya", title="1Man", company="1unreal", address="1Moscow", home="1St. Petersburg",
                            mobile="188888888888", work="189888888888", fax="189988888888", email="1Ivan@gmail.com", email2="1Ivan@mail.ru",
                            email3="1Iban@yandex.ru", homepage="1something", bday="2", bmonth="February", byear="2002", aday="3", amonth="March", ayear="2003"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_new_data = Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya", title="1Man", company="1unreal", address="1Moscow", home="1St. Petersburg",
                            mobile="188888888888", work="189888888888", fax="189988888888", email="1Ivan@gmail.com", email2="1Ivan@mail.ru",
                            email3="1Iban@yandex.ru", homepage="1something", bday="2", bmonth="February", byear="2002", aday="3", amonth="March", ayear="2003")
    app.contact.edit_contact_by_id(contact.id, contact_new_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact_new_data.id = contact.id
    old_contacts = [c if c.id != contact.id else contact_new_data for c in old_contacts]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)