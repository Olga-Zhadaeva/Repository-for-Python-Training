from model.contact import Contact
from random import randrange

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya", title="1Man", company="1unreal", address="1Moscow", home="1St. Petersburg",
                            mobile="188888888888", work="189888888888", fax="189988888888", email="1Ivan@gmail.com", email2="1Ivan@mail.ru",
                            email3="1Iban@yandex.ru", homepage="1something", bday="2", bmonth="February", byear="2002", aday="3", amonth="March", ayear="2003"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya", title="1Man", company="1unreal", address="1Moscow", home="1St. Petersburg",
                            mobile="188888888888", work="189888888888", fax="189988888888", email="1Ivan@gmail.com", email2="1Ivan@mail.ru",
                            email3="1Iban@yandex.ru", homepage="1something", bday="2", bmonth="February", byear="2002", aday="3", amonth="March", ayear="2003")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)