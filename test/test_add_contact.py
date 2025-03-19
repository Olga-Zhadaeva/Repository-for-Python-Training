# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanya", title="Man", company="unreal", address="Moscow", home="St. Petersburg",
                            mobile="88888888888", work="89888888888", fax="89988888888", email="Ivan@gmail.com", email2="Ivan@mail.ru",
                            email3="Iban@yandex.ru", homepage="something", bday="1", bmonth="January", byear="2000", aday="2", amonth="February", ayear="2000"))
    app.session.logout()